import subprocess
import yaml
import os
import shutil
from rich.console import Console

c = Console()
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/tools")

def get_install_command(package_name):
    # Detect the system's package manager
    if shutil.which("pacman"):
        return ["sudo", "pacman", "-S", "--noconfirm", package_name], "pacman"
    elif shutil.which("apt-get"):
        return ["sudo", "apt-get", "install", "-y", package_name], "apt"
    elif shutil.which("dnf"):
        return ["sudo", "dnf", "install", "-y", package_name], "dnf"
    elif shutil.which("zypper"):
        return ["sudo", "zypper", "install", "-y", package_name], "zypper"
    elif shutil.which("apk"):
        return ["sudo", "apk", "add", package_name], "apk"
    else:
        return None, None

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

    cmd, manager_name = get_install_command(pkg)
    if not cmd:
        c.print("\n  [red]no supported package manager found[/] — please install the package manually:")
        c.print(f"  [dim]{pkg}[/]\n")
        return

    try:
        subprocess.run(cmd, check=True)
        c.print(f"\n  [green]✓[/] {tool_name} installed using {manager_name}\n")
        c.print(f"  run [bold]gyra learn {tool_name}[/] to get started\n")
    except subprocess.CalledProcessError:
        c.print(f"\n  [red]install failed[/] — check your internet connection or run manually:")
        c.print(f"  [dim]{' '.join(cmd)}[/]\n")
    except FileNotFoundError:
        c.print(f"\n  [red]{manager_name} not found[/] — install failed\n")
