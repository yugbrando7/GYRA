# Contributing to GYRA

GYRA is open source and contributions are welcome at every level — code, content, design, or documentation. This guide covers the most common contribution types.

---

## The easiest way to contribute — tool definitions

Tool definitions live in `cli/data/tools/` as YAML files. If you know a tool well enough to explain it clearly, you can contribute without touching any Python.

### YAML structure

```yaml
tool: toolname
package: package-name-in-pacman
category: network-scanning | web | password-cracking | wireless | forensics | exploitation | osint | utilities
description: One line — what this tool does
when_to_use: One line — when in a pentest or CTF you reach for this

commands:
  - cmd: "toolname <target>"
    meaning: What this command does in plain English

  - cmd: "toolname -f <file>"
    meaning: What this does
    flag: "-f"
    flag_meaning: What -f does — shown when user runs 'gyra learn toolname -f'
    combine_with:
      - cmd: "toolname -f file -v"
        meaning: Why you'd combine these flags

after:
  - next-tool
  - another-tool

path: networking
path_step: 3
```

### Rules for tool definitions

- `cmd` fields should be copy-pasteable — use `<placeholder>` for things the user fills in
- `meaning` should be plain English, no jargon unless the term is explained
- `flag_meaning` should explain what the flag does, not just restate its name
- `after` points to what logically comes next — don't add more than 2-3
- Keep it short. If a field needs more than two sentences, it's too long.

### Adding a new tool

1. Fork the repo
2. Create `cli/data/tools/yourtool.yaml` following the structure above
3. Test it: `cd cli && python __main__.py learn yourtool`
4. Open a pull request with a one-line description of the tool

---

## Learning paths

Learning paths live in `cli/data/paths/` and sequence tools in the order a beginner should encounter them. Each path corresponds to a menu section in `gyra`.

```yaml
path: networking
title: Networking
description: How networks work and how to map, analyze, and intercept traffic

steps:
  - step: 1
    tool: netdiscover
    concept: Finding live hosts on a network

  - step: 2
    tool: nmap
    concept: Scanning ports and identifying services

  - step: 3
    tool: netcat
    concept: Raw network connections and shells

  - step: 4
    tool: tcpdump
    concept: Capturing and reading network traffic

  - step: 5
    tool: wireshark
    concept: Deep packet analysis
```

To contribute a path — open an issue first to discuss the sequence before writing it. Paths are opinionated and should be discussed.

---

## Code contributions

The CLI is written in Python and uses:
- `rich` for terminal formatting
- `pyyaml` for reading tool definitions
- `subprocess` for pacman/system calls

### Setup

```bash
git clone https://github.com/yugbrando7/GYRA.git
cd GYRA
pip install rich pyyaml --break-system-packages
cd cli
python __main__.py  # test the menu
python __main__.py learn nmap  # test learn
```

### Structure

```
cli/
├── __main__.py       ← command router, add new commands here
├── commands/
│   ├── learn.py      ← gyra learn logic
│   ├── menu.py       ← interactive menu
│   ├── install.py    ← gyra install
│   └── update.py     ← gyra update
└── data/
    ├── tools/        ← YAML tool definitions
    └── paths/        ← YAML learning paths
```

When adding a new command:
1. Create `cli/commands/yourcommand.py` with a `cmd_yourcommand(args)` function
2. Import and wire it in `cli/__main__.py`
3. Add it to the help output in `print_help()`

### Pull request checklist

- [ ] Tested locally with `python __main__.py`
- [ ] No external dependencies added without discussion
- [ ] Code follows the existing style — no docstrings, keep it readable
- [ ] If adding a command, help text is updated

---

## ISO contributions

Changes to `iso/` affect the base system that ships with GYRA. These need more care — open an issue before making changes to the package list or system config. The goal is to keep the base as small as possible.

---

## Reporting issues

Open a GitHub issue with:
- What you ran
- What you expected
- What actually happened
- Your OS and Python version

---

## Questions

Open a GitHub discussion or an issue tagged `question`. There's no Discord or forum yet.
