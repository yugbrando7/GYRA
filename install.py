import subprocess
import yaml
import os
from rich.console import Console

c = Console()
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/tools")

def cmd_install(args):
    if not args:
        c.print("\n  [red]usage:[/] gyra install <tool>\n")
        return

    tool_name = args[0].lower()
    path = os.path.join(DATA_DIR, f"{tool_name}.yaml")

    if not os.path.exists(path):
        c.print(f"\n  [red]tool not found:[/] {tool_name}")
        c.print("  [dim]check spelling or run 'gyra' to browse available tools[/]\n")
        return

    with open(path) as f:
        tool = yaml.safe_load(f)

    pkg = tool.get("package", tool_name)
    description = tool.get("description", "")

    c.print(f"\n  installing [bold white]{tool_name}[/] — {description}")
    c.print(f"  [dim]package: {pkg}[/]\n")

    try:
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", pkg], check=True)
        c.print(f"\n  [green]✓[/] {tool_name} installed\n")
        c.print(f"  run [bold]gyra learn {tool_name}[/] to get started\n")
    except subprocess.CalledProcessError:
        c.print(f"\n  [red]install failed[/] — check your internet connection or run:")
        c.print(f"  [dim]sudo pacman -S {pkg}[/]\n")
    except FileNotFoundError:
        c.print("\n  [red]pacman not found[/] — are you running GYRA?\n")
