<div align="center">

<div align="center">

# GYRA Linux
### /ˈɡaɪrə/ &nbsp;·&nbsp; Hard G. Rhymes with "tiara".

**Ship almost nothing. Guide users through building a complete system while teaching them.**

**Ship almost nothing. Guide users through building a complete system while teaching them.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Status](https://img.shields.io/badge/status-in%20development-orange)
![Base](https://img.shields.io/badge/base-Arch%20Linux-1793d1)

</div>

---

## What is GYRA?

GYRA is a Linux distribution built around a single idea: you should know everything that's on your system, because you put it there yourself.

It boots into a clean environment — a wallpaper, a terminal, and the GYRA Hub. Nothing else. No desktop full of applications you didn't ask for. No background services you didn't choose. Just a starting point.

From there, the Hub guides you through building your system into exactly what you need — whether that's a development machine, a security lab, a minimal desktop, or something else entirely. Every package installed is one you chose. Every config is one you understand.

GYRA gives you Arch Linux's level of control without Arch Linux's barrier to entry.

---

## The problem with existing distros

Most distros make one of two mistakes.

They ship too much — a full desktop, a suite of applications, services running in the background. You inherit a system someone else designed. You don't know what's there or why. When something breaks, you don't know where to look.

Or they ship too little and leave you completely alone. Arch Linux is powerful precisely because it makes you build everything yourself — but that process is a wall for anyone who hasn't already climbed it.

GYRA sits between these. Minimal by default. Guided by design. You build the system. GYRA teaches you how.

---

## How it works

**Boot** into a clean live environment. Wallpaper. Terminal. The GYRA Hub. Nothing else running, nothing pre-installed beyond what's needed to get you started.

**Open the Hub.** Choose what you want to build — a dev machine, a security setup, a minimal desktop, or start completely from scratch. The Hub doesn't install anything automatically. It presents your options, explains what each one is, and waits for you to decide.

**Install what you choose.** Every package comes with context — what it is, what it does, why you might want it. You're not clicking through an app store. You're making deliberate decisions about your system.

**Learn as you go.** The `gyra` CLI runs in your terminal and teaches you the actual commands behind what you're using. Not wrappers. Not shortcuts. The real thing — with enough context to understand what you're running and why.

---

## The GYRA CLI

The `gyra` command is GYRA's teaching interface. Run it alone to open the guided menu. Use it to learn any tool on your system.

```
gyra
```
```
  ██████╗ ██╗   ██╗██████╗  █████╗
 ██╔════╝ ╚██╗ ██╔╝██╔══██╗██╔══██╗
 ██║  ███╗ ╚████╔╝ ██████╔╝███████║
 ██║   ██║  ╚██╔╝  ██╔══██╗██╔══██║
 ╚██████╔╝   ██║   ██║  ██║██║  ██║
  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝

  1. Linux Fundamentals
  2. Networking
  3. Web Security
  4. Exploitation
  5. Forensics & Reverse Engineering
  6. OSINT
  7. Install Tools
  8. Documentation
  9. My Progress

  →
```

```bash
gyra learn nmap          # what nmap is, every important command, when to use it
gyra learn nmap -sV      # what this specific flag does and why it matters
gyra learn -b nmap       # brief two-line reference
gyra learn -b nmap -sV   # one-line flag reminder
```

GYRA teaches real commands with real context. When you move to any other system, you already know the tools — you just lose the guided context, which you no longer need.

---

## Editions

GYRA base is distribution-agnostic. Editions are curated paths through the Hub — a structured set of packages, configs, and learning content organized around a purpose.

| Edition | Purpose |
|---|---|
| **Security** | Penetration testing, CTFs, cybersecurity learning |
| **Development** | Languages, editors, version control, containers |
| **Desktop** | Minimal GUI, window managers, theming |
| **Server** | Headless, services, networking tools |

Editions are not pre-installed profiles. They are guided paths. You still choose every package. The edition just organizes the choices and provides the learning content around them.

---

## What GYRA is not

- Not a beginner distro that hides complexity behind GUIs
- Not a security distro that ships 300 tools you'll never use
- Not an opinionated desktop with someone else's defaults
- Not a shortcut to avoid learning how Linux works

---

## Project structure

```
gyra/
├── iso/          # archiso profile — packages, airootfs, boot config
├── hub/          # GYRA Hub application (PyQt6)
├── installer/    # Calamares installer configuration
├── cli/          # gyra CLI — learning paths and tool definitions
├── editions/     # edition definitions (YAML)
├── assets/       # logo, wallpaper, icons, fonts
└── docs/         # build instructions, contribution guide
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
| GYRA Hub — system builder GUI | 🔲 Planned |
| GYRA CLI — learning interface | 🔲 Planned |
| GYRA Installer (Calamares) | 🔲 Planned |
| Security edition — learning paths | 🔲 Planned |
| Public release | 🔲 Planned |

---

## Contributing

GYRA is in early development. Contributions are welcome in any form.

The easiest way to contribute is through content — edition definitions, tool descriptions, and learning path entries live as YAML files in `editions/` and `cli/`. No Python required. If you know a tool well enough to explain it clearly in three lines, you can contribute to GYRA.

Code contributions, bug reports, and design feedback are equally welcome. Details coming in `docs/CONTRIBUTING.md`.

---

## License

GYRA is licensed under the [GNU General Public License v3.0](LICENSE).

---

<div align="center">
<sub>Ship almost nothing. Teach everything.</sub>
</div>
