# Building GYRA

This guide covers how to build the GYRA ISO from source.

---

## Requirements

- An Arch Linux system or VM (GYRA is built on Arch — you need Arch to build it)
- At least 4GB RAM and 15GB free disk space for the build process
- `archiso` installed

If you're on Windows, set up an Arch VM first. See the section at the bottom.

---

## Setup

Install archiso:

```bash
sudo pacman -S archiso
```

Clone the repo:

```bash
git clone https://github.com/yugbrando7/GYRA.git
cd GYRA
```

---

## Build

```bash
sudo mkarchiso -v -w /tmp/gyra-work -o ./out iso/
```

- `-v` verbose output so you can see what's happening
- `-w` working directory — temp files go here, needs ~8GB free
- `-o` output directory — the finished ISO lands here

The build takes 5–15 minutes depending on your connection and hardware.

---

## Test without burning

Test the ISO in QEMU before touching real hardware:

```bash
# Install QEMU if you don't have it
sudo pacman -S qemu-full

# Boot the ISO
qemu-system-x86_64 \
  -m 2G \
  -cdrom out/gyra-*.iso \
  -boot d \
  -enable-kvm
```

Remove `-enable-kvm` if you're on a VM that doesn't support nested virtualization.

---

## Clean build artifacts

The working directory and ISO are gitignored. To clean up manually:

```bash
sudo rm -rf /tmp/gyra-work
rm -rf ./out
```

---

## Installing the gyra CLI for development

During development you can run the CLI directly without installing it:

```bash
cd cli
python __main__.py learn nmap
python __main__.py
```

To install it system-wide on Arch for testing:

```bash
sudo pip install rich pyyaml --break-system-packages
sudo cp -r cli/ /usr/lib/gyra/
sudo ln -sf /usr/lib/gyra/__main__.py /usr/local/bin/gyra
```

---

## Building on Windows

You need an Arch Linux VM. Recommended setup:

1. Install VirtualBox (free) or VMware Workstation Pro (free for personal use)
2. Download the Arch Linux ISO from archlinux.org
3. Install Arch in the VM — give it at least 4GB RAM and 30GB disk
4. Set up SSH access and use VS Code Remote-SSH to edit files from Windows
5. Run all build commands inside the VM

The ISO output can be copied to your Windows host via the VM's shared folder.

---

## Troubleshooting

**`mkarchiso: command not found`** — install archiso: `sudo pacman -S archiso`

**Build fails partway through** — clean the work directory and retry:
```bash
sudo rm -rf /tmp/gyra-work && sudo mkarchiso -v -w /tmp/gyra-work -o ./out iso/
```

**QEMU boots but keyboard doesn't work** — add `-usb -device usb-kbd` to the QEMU command.

**Out of disk space** — the work directory needs ~8GB. Point `-w` somewhere with more space.
