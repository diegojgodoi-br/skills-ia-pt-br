# Runbook VMware → Proxmox VE

## 0. Preparação (uma vez)

- [ ] Proxmox VE 8.2 ou superior atualizado em todos os nós (`apt update && apt full-upgrade`).
- [ ] Bridges e VLANs criadas com os mesmos nomes/IDs dos port groups do VMware (mapa port group → bridge/VLAN).
- [ ] Storage de destino criado e testado (ZFS, Ceph, LVM-thin, NFS/iSCSI).
- [ ] ISO `virtio-win` enviada para o storage de ISOs.
- [ ] Backup configurado no destino (Proxmox Backup Server ou Veeam com suporte a Proxmox).
- [ ] Adicionar a origem: **Datacenter › Storage › Add › ESXi** (servidor, usuário administrador, senha). Aceite o certificado ou desmarque a verificação só se a rede for confiável. As VMs aparecem sob esse storage.

## 1. Antes de desligar a VM (no VMware)

**Windows**
- [ ] Montar a ISO virtio-win e rodar `virtio-win-guest-tools.exe` (drivers + qemu-guest-agent).
- [ ] Anotar IP, máscara, gateway e DNS (`ipconfig /all`). Se houver reserva DHCP, anotar o MAC.
- [ ] Ter a chave de recuperação do BitLocker, se houver.

**Linux**
- [ ] Confirmar virtio no initramfs: `lsinitramfs /boot/initrd.img-$(uname -r) | grep virtio` (Debian/Ubuntu) ou `lsinitrd | grep virtio` (RHEL). Se faltar, incluir e regenerar (`update-initramfs -u` / `dracut -f`).
- [ ] Anotar a configuração de rede e o nome da interface.

**Todas**
- [ ] Remover snapshots no VMware.
- [ ] Desligar a VM (desligamento normal, não forçado).

## 2. Importar (no Proxmox)

1. Selecione a VM sob o storage ESXi › **Import**.
2. Ajuste antes de importar:
   - **CPU:** `x86-64-v2-AES` (ou `host` se todos os nós forem iguais).
   - **BIOS:** OVMF + disco EFI se a VM era UEFI; SeaBIOS se era BIOS.
   - **Máquina:** q35 para UEFI/Windows.
   - **Disco:** controlador VirtIO SCSI single, `discard` e `iothread` ligados. Para Windows, primeiro boot em **SATA**.
   - **Rede:** VirtIO na bridge/VLAN certa (Windows sem driver: e1000).
   - **Storage de destino** e formato (raw em ZFS/LVM; qcow2 se quiser snapshot em diretório/NFS).
3. Deixe **importação ao vivo desmarcada** em produção, exceto se a parada for inaceitável e a VM não for banco de dados.
4. Importe no máximo 4 discos por vez.

Alternativa sem o wizard: copiar o `.vmdk` e usar `qm disk import <vmid> <arquivo.vmdk> <storage>`, depois anexar o disco em Hardware e ajustar a ordem de boot.

## 3. Primeiro boot

**Windows**
- [ ] Ligar com disco em SATA. Confirmar drivers no Gerenciador de Dispositivos.
- [ ] Para trocar para VirtIO SCSI: adicionar um disco pequeno (1 GB) em SCSI, ligar, confirmar driver, desligar, remover o disco extra, mudar o disco do sistema para SCSI e ajustar a ordem de boot.
- [ ] Configurar o IP na placa nova. Se o Windows reclamar de IP em uso, remover a placa antiga oculta.
- [ ] Desinstalar o VMware Tools.
- [ ] Ligar o **QEMU Guest Agent** em Options da VM.

**Linux**
- [ ] Ajustar o nome da interface (`ens18`) em `/etc/netplan/*.yaml` ou `/etc/network/interfaces`.
- [ ] `apt install qemu-guest-agent` (ou `dnf`), habilitar e remover `open-vm-tools`.

## 4. Validar

- [ ] Serviço responde (aplicação, porta, login do usuário-chave).
- [ ] DNS, AD, horário (NTP) e compartilhamentos.
- [ ] Backup do Proxmox rodou e foi testada uma restauração.
- [ ] Monitoramento apontando para a nova VM.

## 5. Rollback

- Desligar a VM no Proxmox e religar a original no VMware (ela não foi apagada).
- Prazo para remover a VM antiga do VMware: definir com o dono do serviço (ex.: 7 dias).

## Problemas comuns

| Sintoma | Causa provável | Correção |
|---|---|---|
| Windows dá tela azul INACCESSIBLE_BOOT_DEVICE | disco em VirtIO sem driver | voltar o disco para SATA, instalar driver, trocar depois |
| "No bootable device" | VM era UEFI e subiu em SeaBIOS (ou o contrário) | trocar BIOS para OVMF e adicionar disco EFI |
| Linux sem rede | interface mudou de nome | ajustar netplan/interfaces para ens18 |
| Linux cai no shell do initramfs | faltam módulos virtio | boot com disco em SATA, incluir virtio e regenerar o initramfs |
| Importação falha em VM de vSAN | wizard não lê vSAN | mover a VM para datastore local/NFS antes |
| Windows pede reativação | hardware virtual mudou | reativar com a licença vigente |
