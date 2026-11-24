#!/usr/bin/env python3
"""Lê o inventário do VMware (aba vInfo do RVTools, em .xlsx ou .csv) e monta o plano de migração para Proxmox VE.

Uso:
  python3 inventario_vmware.py RVTools_export.xlsx
  python3 inventario_vmware.py vInfo.csv --banda-gbps 10 --md plano.md --csv vms.csv

Para cada VM: tamanho, sistema, firmware (BIOS/UEFI), riscos e a configuração sugerida no Proxmox.
Agrupa em ondas (piloto -> simples -> críticas/complexas) e estima o tempo de cópia pela banda.
Só biblioteca padrão; não se conecta a nada.
"""
import argparse
import csv
import io
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# nomes de coluna aceitos (RVTools muda um pouco entre versões)
COLS = {
    "vm": ["vm", "vm name", "name"],
    "power": ["powerstate", "power state"],
    "template": ["template"],
    "cpus": ["cpus", "num cpu", "cpu"],
    "mem_mb": ["memory", "memory mb", "mem mb"],
    "nics": ["nics", "# nics"],
    "discos": ["disks", "# disks"],
    "prov_mb": ["provisioned mb", "provisioned mib"],
    "uso_mb": ["in use mb", "in use mib"],
    "os_cfg": ["os according to the configuration file", "os"],
    "os_tools": ["os according to the vmware tools", "guest os"],
    "firmware": ["firmware"],
    "hw": ["hw version", "hardware version"],
    "ip": ["primary ip address", "ip address"],
    "cluster": ["cluster"],
    "host": ["host"],
    "path": ["path", "vm path"],
    "nota": ["annotation", "notes"],
}

SO_ANTIGO = re.compile(r"windows (server )?(2003|2008|xp|vista|7)\b|centos.*\b[56]\b|red hat.*\b[56]\b|"
                       r"ubuntu.*\b(1[0-6])\.|debian.*\b[5-8]\b|freebsd", re.I)
CRITICA = re.compile(r"\b(sql|db|banco|oracle|erp|ad|dc\d*|domain|exchange|sap|totvs|protheus|fiscal)\b", re.I)


def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


# ---------- leitura .xlsx mínima (sem openpyxl) ----------

def _ler_xlsx(caminho, aba="vInfo"):
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    with zipfile.ZipFile(caminho) as z:
        compart = []
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", ns):
                compart.append("".join(t.text or "" for t in si.iter(f"{{{ns['m']}}}t")))
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        alvo = {r.get("Id"): r.get("Target") for r in rels}
        folhas = [(s.get("name"), alvo[s.get(f"{{{ns['r']}}}id")]) for s in wb.find("m:sheets", ns)]
        escolhida = next((t for n, t in folhas if n.lower() == aba.lower()), folhas[0][1])
        escolhida = escolhida.lstrip("/")
        if not escolhida.startswith("xl/"):
            escolhida = "xl/" + escolhida
        dados = ET.fromstring(z.read(escolhida))
    linhas = []
    for row in dados.iter(f"{{{ns['m']}}}row"):
        vals = {}
        for c in row.findall("m:c", ns):
            ref = re.match(r"([A-Z]+)", c.get("r", "A")).group(1)
            col = 0
            for ch in ref:
                col = col * 26 + ord(ch) - 64
            v = c.find("m:v", ns)
            texto = v.text if v is not None else ""
            if c.get("t") == "s" and texto:
                texto = compart[int(texto)]
            elif c.get("t") == "inlineStr":
                texto = "".join(t.text or "" for t in c.iter(f"{{{ns['m']}}}t"))
            vals[col] = texto or ""
        if vals:
            linhas.append([vals.get(i, "") for i in range(1, max(vals) + 1)])
    return linhas


def _ler_csv(caminho):
    bruto = Path(caminho).read_bytes()
    for enc in ("utf-8-sig", "cp1252"):
        try:
            texto = bruto.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    sep = ";" if texto.splitlines()[0].count(";") > texto.splitlines()[0].count(",") else ","
    return list(csv.reader(io.StringIO(texto), delimiter=sep))


def carregar(caminho):
    linhas = _ler_xlsx(caminho) if str(caminho).lower().endswith((".xlsx", ".xlsm")) else _ler_csv(caminho)
    if not linhas:
        raise ValueError("arquivo vazio")
    cab = [_norm(c) for c in linhas[0]]
    idx = {}
    for chave, nomes in COLS.items():
        for n in nomes:
            if n in cab:
                idx[chave] = cab.index(n)
                break
    if "vm" not in idx:
        raise ValueError("não achei a coluna 'VM'. Exporte a aba vInfo do RVTools.")
    vms = []
    for l in linhas[1:]:
        if not any(x.strip() for x in l):
            continue
        vms.append({k: (l[i].strip() if i < len(l) else "") for k, i in idx.items()})
    return vms


def _num(s):
    s = (s or "").replace(".", "").replace(",", ".") if re.fullmatch(r"[\d.]+,\d+", s or "") else (s or "")
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return 0.0


def analisar(vm):
    so = vm.get("os_tools") or vm.get("os_cfg") or ""
    windows = "windows" in so.lower()
    fw = (vm.get("firmware") or "").lower()
    uefi = fw == "efi" or "uefi" in fw
    uso_gb = _num(vm.get("uso_mb")) / 1024 or _num(vm.get("prov_mb")) / 1024
    prov_gb = _num(vm.get("prov_mb")) / 1024
    ligada = (vm.get("power") or "").lower() in ("poweredon", "ligada", "on")
    riscos, passos = [], []
    if (vm.get("template") or "").lower() in ("true", "verdadeiro", "sim", "1"):
        riscos.append("template: converta em VM ou recrie no Proxmox")
    if "vsan" in (vm.get("path") or "").lower():
        riscos.append("disco em vSAN: o import wizard não lê; mova para datastore local/NFS antes")
    if SO_ANTIGO.search(so):
        riscos.append(f"SO antigo ({so}): drivers VirtIO podem não existir; comece com IDE/SATA e e1000")
    if prov_gb > 2048:
        riscos.append(f"disco grande ({prov_gb:,.0f} GB provisionados): planeje janela longa ou importação ao vivo")
    if _num(vm.get("discos")) > 4:
        riscos.append("mais de 4 discos: importe em etapas")
    if _num(vm.get("nics")) > 1:
        riscos.append("várias placas de rede: mapeie cada uma para a bridge/VLAN certa")
    if CRITICA.search(f"{vm.get('vm', '')} {vm.get('nota', '')}"):
        riscos.append("parece serviço crítico (banco, AD, ERP): migrar por último, com teste e rollback")
    if windows:
        passos += ["antes: instalar virtio-win (drivers + qemu-guest-agent) com a VM ainda no VMware",
                   "anotar IP fixo; a placa nova recebe outro nome",
                   "1º boot no Proxmox com disco em SATA; depois trocar para VirtIO SCSI single",
                   "remover VMware Tools depois que a VM subir no Proxmox"]
    else:
        passos += ["conferir módulos virtio no initramfs (virtio_scsi, virtio_net) antes de desligar",
                   "ajustar nome da interface (ens192/ens160 -> ens18) no netplan/interfaces",
                   "instalar qemu-guest-agent e remover open-vm-tools"]
    config = {
        "bios": "OVMF (UEFI) + disco EFI" if uefi else "SeaBIOS",
        "maquina": "q35" if uefi or windows else "i440fx ou q35",
        "cpu": "x86-64-v2-AES (ou host se o cluster for homogêneo)",
        "disco": "VirtIO SCSI single, discard e iothread ligados",
        "rede": "VirtIO (Windows: e1000 até instalar o driver)",
    }
    pontos = len(riscos) + (2 if uso_gb > 500 else 0) + (1 if ligada else 0)
    return {"vm": vm.get("vm"), "so": so or "desconhecido", "ligada": ligada, "uefi": uefi,
            "cpus": vm.get("cpus", ""), "memoria_gb": round(_num(vm.get("mem_mb")) / 1024, 1),
            "uso_gb": round(uso_gb, 1), "provisionado_gb": round(prov_gb, 1),
            "riscos": riscos, "passos": passos, "config_proxmox": config, "complexidade": pontos,
            "host": vm.get("host", ""), "cluster": vm.get("cluster", "")}


def horas_copia(gb, banda_gbps, eficiencia=0.6):
    """Estimativa grosseira: GB em uso / (banda x eficiência)."""
    return gb * 8 / (banda_gbps * eficiencia) / 3600


def planejar(vms, banda_gbps=1.0):
    analisadas = [analisar(v) for v in vms]
    for a in analisadas:
        a["horas_copia"] = round(horas_copia(a["uso_gb"], banda_gbps), 2)
        a["min_copia"] = max(1, round(horas_copia(a["uso_gb"], banda_gbps) * 60))
    candidatas = sorted((a for a in analisadas if not a["riscos"]), key=lambda a: a["uso_gb"])
    piloto = candidatas[:min(3, len(candidatas))]
    resto = [a for a in analisadas if a not in piloto]
    simples = [a for a in resto if a["complexidade"] <= 1 and not any("crítico" in r for r in a["riscos"])]
    complexas = [a for a in resto if a not in simples]
    ondas = [("Onda 0 – piloto", piloto), ("Onda 1 – simples", sorted(simples, key=lambda a: a["uso_gb"])),
             ("Onda 2 – críticas e complexas", sorted(complexas, key=lambda a: a["complexidade"]))]
    resumo = {"vms": len(analisadas), "uso_total_gb": round(sum(a["uso_gb"] for a in analisadas), 1),
              "vcpus": int(sum(_num(str(a["cpus"])) for a in analisadas)),
              "memoria_gb": round(sum(a["memoria_gb"] for a in analisadas), 1),
              "windows": sum("windows" in a["so"].lower() for a in analisadas),
              "uefi": sum(a["uefi"] for a in analisadas),
              "com_risco": sum(bool(a["riscos"]) for a in analisadas),
              "horas_copia_total": round(sum(a["horas_copia"] for a in analisadas), 1),
              "banda_gbps": banda_gbps}
    return resumo, ondas


def markdown(resumo, ondas):
    r = resumo
    out = ["# Plano de migração VMware → Proxmox VE", "",
           f"**{r['vms']} VMs** · {r['vcpus']} vCPUs · {r['memoria_gb']} GB de RAM · "
           f"{r['uso_total_gb']} GB em uso · {r['windows']} Windows · {r['uefi']} UEFI · "
           f"{r['com_risco']} com pontos de atenção", "",
           f"Cópia estimada: **~{r['horas_copia_total']} h** a {r['banda_gbps']} Gbps (60% de eficiência). "
           "É só a transferência; some boot, testes e ajustes.", ""]
    for titulo, lista in ondas:
        out += [f"## {titulo} ({len(lista)} VMs)", ""]
        if not lista:
            out += ["_nenhuma_", ""]
            continue
        out += ["| VM | SO | Em uso (GB) | Cópia (min) | Firmware | Pontos de atenção |", "|---|---|---|---|---|---|"]
        for a in lista:
            out.append(f"| {a['vm']} | {a['so']} | {a['uso_gb']} | {a['min_copia']} | "
                       f"{'UEFI' if a['uefi'] else 'BIOS'} | {'; '.join(a['riscos']) or '—'} |")
        out.append("")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("--banda-gbps", type=float, default=1.0)
    ap.add_argument("--md")
    ap.add_argument("--csv")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        vms = carregar(a.arquivo)
    except (ValueError, KeyError, zipfile.BadZipFile, OSError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2
    resumo, ondas = planejar(vms, a.banda_gbps)
    if a.json:
        print(json.dumps({"resumo": resumo, "ondas": {t: l for t, l in ondas}}, ensure_ascii=False, indent=2))
    else:
        print(markdown(resumo, ondas))
    if a.md:
        Path(a.md).write_text(markdown(resumo, ondas), encoding="utf-8")
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["onda", "vm", "so", "ligada", "uefi", "cpus", "memoria_gb", "uso_gb", "horas_copia",
                        "bios", "disco", "rede", "pontos_de_atencao", "passos"])
            for t, lista in ondas:
                for v in lista:
                    c = v["config_proxmox"]
                    w.writerow([t, v["vm"], v["so"], v["ligada"], v["uefi"], v["cpus"],
                                str(v["memoria_gb"]).replace(".", ","), str(v["uso_gb"]).replace(".", ","),
                                str(v["horas_copia"]).replace(".", ","), c["bios"], c["disco"], c["rede"],
                                " | ".join(v["riscos"]), " | ".join(v["passos"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
