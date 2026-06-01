import subprocess
from rich.console import Console

c = Console()

REPO = "https://github.com/yugbrando7/GYRA.git"

def cmd_update():
    c.print("\n  [bold white]gyra update[/]")
    c.print("  [dim]pulling latest CLI and tool definitions...[/]\n")

    try:
        result = subprocess.run(
            ["sudo", "pacman", "-Sy", "--noconfirm", "gyra"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            c.print("  [green]✓[/] GYRA is up to date\n")
        else:
            # Fallback: pull from git if pacman package not yet set up
            c.print("  [dim]pacman package not found, trying git...[/]")
            subprocess.run(["git", "-C", "/usr/lib/gyra", "pull"], check=True)
            c.print("  [green]✓[/] updated from git\n")
    except Exception as e:
        c.print(f"  [red]update failed:[/] {e}")
        c.print(f"  [dim]you can manually pull from {REPO}[/]\n")
