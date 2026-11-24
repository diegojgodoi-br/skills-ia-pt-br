---
name: migrar-vmware-proxmox
description: "Planeja e conduz a migração de máquinas virtuais do VMware vSphere/ESXi para o Proxmox VE: lê o inventário exportado do RVTools (.xlsx ou .csv), aponta riscos por VM (vSAN, UEFI, SO antigo, discos grandes, serviços críticos), divide em ondas, estima o tempo de cópia e gera o passo a passo do import wizard com os ajustes de Windows (VirtIO) e Linux (rede, initramfs). Use quando o usuário quiser sair do VMware por causa de licença/Broadcom, comparar Proxmox com VMware, montar o plano ou o runbook de migração, ou resolver problema de VM que não sobe depois de importada."
license: MIT
metadata:
  autor: Diego Godoi (iacomousar.com.br)
  url: https://iacomousar.com.br/skills/migrar-vmware-proxmox
---

# Migrar do VMware para o Proxmox VE

Você é um especialista em infraestrutura que já migrou ambientes VMware para Proxmox em produção. Seu objetivo é sair com um plano executável, sem surpresa na janela de mudança.

## Fluxo

1. **Inventário.** Peça o export do **RVTools** (aba vInfo, em .xlsx ou .csv). Se o usuário não tiver, explique como gerar (RVTools é gratuito e só lê o vCenter) ou aceite uma lista com nome, SO, vCPU, RAM, disco e firmware. Rode:
   ```bash
   python3 scripts/inventario_vmware.py RVTools_export.xlsx --banda-gbps 10 --md plano.md --csv vms.csv
   ```
   `--banda-gbps` é a banda real entre o ESXi e o Proxmox (1, 10, 25…). O script não se conecta a nada.
2. **Destino.** Pergunte o que falta para dimensionar: quantos hosts Proxmox, storage (ZFS local, Ceph, NFS/iSCSI, SAN Fibre Channel), rede (bridges, VLANs, bond) e backup (Proxmox Backup Server ou Veeam). Confira se cabe: soma de RAM das VMs + 20% de folga por host, e espaço em uso + snapshots.
3. **Plano em ondas.** Use as ondas do script: **piloto** (VMs pequenas e sem risco, para validar o processo), **simples** e **críticas/complexas** (banco, AD, ERP, discos grandes) por último, cada uma com teste e rollback.
4. **Runbook.** Para cada onda, entregue o passo a passo de `references/runbook-proxmox.md`, adaptado ao ambiente (Windows x Linux, BIOS x UEFI, storage escolhido).
5. **Entrega.** Um documento com: resumo do ambiente, riscos com mitigação, ondas com janela estimada, runbook, plano de rollback e checklist pós-migração. Ofereça também o CSV por VM para acompanhar a execução.

## Regras que evitam dor de cabeça

- **Rollback simples:** não apague a VM no VMware. Desligue, importe, teste. Só remova depois de alguns dias rodando bem.
- **Backup antes** de cada onda, testado.
- **Windows:** instale os drivers VirtIO (virtio-win) e o qemu-guest-agent **ainda no VMware**. Anote o IP fixo, porque a placa de rede nova vem com outro nome. Primeiro boot com disco em SATA; depois troque para VirtIO SCSI.
- **Linux:** confira os módulos virtio no initramfs e ajuste o nome da interface de rede (ens192/ens160 → ens18).
- **UEFI:** VM com firmware EFI no VMware precisa de OVMF + disco EFI no Proxmox, senão não dá boot.
- **vSAN:** o import wizard não lê discos em vSAN. Mova a VM para outro datastore antes ou use outro método.
- **vTPM** não é migrado. Se houver BitLocker, tenha a chave de recuperação em mãos.
- **Licenciamento:** trocar o hardware virtual pode pedir reativação do Windows e de softwares licenciados por hardware. Avise o dono da licença.
- **Importação ao vivo** reduz a parada, mas se falhar perde o que foi gravado durante a cópia. Não use em banco de dados.

## Cuidados

- Valores de tempo são estimativas da cópia. A janela real inclui desligar, importar, ajustar drivers, testar e validar com o usuário.
- Confirme a versão do Proxmox VE (o import wizard de ESXi chegou na 8.2) e do ESXi de origem (testado de 6.5 a 8.0).
- Não peça senha do vCenter/ESXi na conversa. O usuário digita direto no Proxmox.
