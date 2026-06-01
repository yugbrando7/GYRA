from rich.console import Console
from rich.text import Text

c = Console()

BANNER = """
  ██████╗ ██╗   ██╗██████╗  █████╗
 ██╔════╝ ╚██╗ ██╔╝██╔══██╗██╔══██╗
 ██║  ███╗ ╚████╔╝ ██████╔╝███████║
 ██║   ██║  ╚██╔╝  ██╔══██╗██╔══██║
 ╚██████╔╝   ██║   ██║  ██║██║  ██║
  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
"""

MENU = [
    ("1", "Linux Fundamentals"),
    ("2", "Networking"),
    ("3", "Web Security"),
    ("4", "Exploitation"),
    ("5", "Forensics & Reverse Engineering"),
    ("6", "OSINT"),
    ("7", "Install Tools"),
    ("8", "Documentation"),
    ("9", "My Progress"),
]

def cmd_menu():
    c.print(f"[bold white]{BANNER}[/]")
    c.print("  [dim]Ship almost nothing. Teach everything.[/]\n")

    for num, label in MENU:
        c.print(f"  [bold white]{num}.[/]  {label}")

    c.print()
    try:
        choice = input("  → ").strip()
    except (KeyboardInterrupt, EOFError):
        c.print("\n")
        return

    handle_choice(choice)

def handle_choice(choice):
    mapping = {item[0]: item[1] for item in MENU}
    if choice not in mapping:
        c.print(f"\n  [red]invalid option:[/] {choice}\n")
        return

    label = mapping[choice]

    # Placeholder — each section will be built out
    c.print(f"\n  [bold white]{label}[/]")
    c.print(f"  [dim]{'─' * 36}[/]")
    c.print("  [dim]coming soon — this section is being built[/]\n")
    c.print("  [dim]run 'gyra update' to get the latest content[/]\n")
