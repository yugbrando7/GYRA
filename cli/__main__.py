#!/usr/bin/env python3
import sys
from commands.learn import cmd_learn
from commands.menu import cmd_menu
from commands.install import cmd_install
from commands.update import cmd_update

def main():
    args = sys.argv[1:]

    if not args:
        cmd_menu()
        return

    command = args[0]

    if command == "learn":
        cmd_learn(args[1:])
    elif command == "install":
        cmd_install(args[1:])
    elif command == "update":
        cmd_update()
    elif command in ("-h", "--help", "help"):
        print_help()
    else:
        from rich.console import Console
        Console().print(f"\n  [red]unknown command:[/] '{command}'")
        Console().print("  run [bold]gyra[/] to open the menu\n")

def print_help():
    from rich.console import Console
    c = Console()
    c.print("\n  [bold white]gyra[/] — GYRA Linux CLI\n")
    c.print("  [dim]usage:[/]")
    c.print("    gyra                         open the interactive menu")
    c.print("    gyra learn <tool>            learn a tool — commands, flags, context")
    c.print("    gyra learn <tool> <flag>     learn a specific flag")
    c.print("    gyra learn -b <tool>         brief two-line reference")
    c.print("    gyra learn -b <tool> <flag>  one-line flag reminder")
    c.print("    gyra install <tool>          install a tool")
    c.print("    gyra update                  pull latest CLI and definitions\n")

if __name__ == "__main__":
    main()
