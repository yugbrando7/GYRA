<div align="center">

# GYRA

**An ultra-lightweight, modular Linux distribution built around user choice.**

*Start with nothing. Build exactly what you need.*

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Status](https://img.shields.io/badge/status-in%20development-orange)
![Base](https://img.shields.io/badge/base-Arch%20Linux-1793d1)

</div>

---

## What is GYRA?

GYRA is a Linux distribution that boots into a clean, minimal live environment and gives you a single tool — the **GYRA Hub** — to build your system from scratch. No bloat, no assumptions, no pre-installed software you'll never use.

Instead of shipping a system full of applications, GYRA ships a starting point. You decide what goes on it.

**GYRA Security Edition** is the first edition of GYRA, focused on cybersecurity and penetration testing. It is designed as a beginner-friendly alternative to distributions like Kali Linux — less overwhelming, more guided, equally capable.

---

## Philosophy

- **Minimal by default.** The base system is as small as it can be while still being functional.
- **User-driven.** Every piece of software on your system was put there by you, intentionally.
- **Beginner-friendly.** Tools come with context — not just a name, but a description of what they do and when to use them.
- **Learn by using.** GYRA is built alongside its own creator's growing knowledge of Linux and cybersecurity. The distro grows as you do.

---

## Features (planned)

- Clean live environment — wallpaper, terminal, and the GYRA Hub. Nothing else.
- **GYRA Hub** — a lightweight native GUI for installing drivers, tools, and packages by category
- **GYRA Installer** — a simplified, guided installer for putting GYRA on real hardware
- Curated cybersecurity tool library with beginner-friendly descriptions
- Guided learning paths — install tools in a logical order as you learn the concepts behind them
- Rolling release base via Arch Linux
- Fully open source and community-driven

---

## Project structure

```
gyra/
├── iso/          # archiso profile — packages, airootfs, boot config
├── hub/          # GYRA Hub application (PyQt6)
├── installer/    # Calamares installer configuration
├── tools/        # Tool definitions and learning path data (YAML)
├── assets/       # Logo, wallpaper, icons, fonts
└── docs/         # Build instructions, contribution guide
```

---

## Building GYRA

> **Requirements:** An Arch Linux system (or VM) with `archiso` installed.

```bash
# Install archiso
sudo pacman -S archiso

# Clone the repo
git clone https://github.com/yugbrando7/GYRA.git
cd GYRA

# Build the ISO
sudo mkarchiso -v -w /tmp/gyra-work -o ./out iso/

# Test in QEMU
qemu-system-x86_64 -m 2G -cdrom out/gyra-*.iso -boot d
```

---

## Roadmap

| Phase | Status |
|---|---|
| Dev environment & VM setup | 🔲 In progress |
| archiso base & first boot | 🔲 Planned |
| Live session & branding | 🔲 Planned |
| GYRA Hub — core GUI | 🔲 Planned |
| Package install backend | 🔲 Planned |
| GYRA Installer (Calamares) | 🔲 Planned |
| Learning paths & tool descriptions | 🔲 Planned |
| Public release | 🔲 Planned |

---

## Contributing

GYRA is in early development. Contributions are welcome in any form — code, tool descriptions, learning path content, design, or documentation.

If you want to add a tool to the Hub or write a learning path entry, you don't need to touch any Python — tool definitions live in YAML files in `tools/`. More details coming in `docs/CONTRIBUTING.md`.

---

## License

GYRA is licensed under the [GNU General Public License v3.0](LICENSE).

---

<div align="center">
<sub>Built from scratch. Learned along the way.</sub>
</div>
