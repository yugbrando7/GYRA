import yaml
import os
from rich.console import Console
from rich.rule import Rule

c = Console()

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/tools")

def load_tool(name):
    path = os.path.join(DATA_DIR, f"{name}.yaml")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return yaml.safe_load(f)

def cmd_learn(args):
    if not args:
        c.print("\n  [red]usage:[/] gyra learn [-b] <tool> [flag]\n")
        return

    brief = False
    if args[0] == "-b":
        brief = True
        args = args[1:]

    if not args:
        c.print("\n  [red]usage:[/] gyra learn [-b] <tool> [flag]\n")
        return

    tool_name = args[0].lower()
    flag = args[1] if len(args) > 1 else None

    tool = load_tool(tool_name)
    if not tool:
        c.print(f"\n  [red]no entry found for:[/] {tool_name}")
        c.print(f"  [dim]contributions welcome — add {tool_name}.yaml to cli/data/tools/[/]\n")
        return

    if flag:
        show_flag(tool, flag, brief)
    else:
        show_tool(tool, brief)

def show_tool(tool, brief):
    if brief:
        # Two lines max
        c.print(f"\n  [bold white]{tool['tool']}[/] — {tool['description']}")
        cores = "  ·  ".join(
            f"[dim]{cmd['cmd']}[/]" for cmd in tool['commands'][:4]
        )
        c.print(f"  core: {cores}\n")
        return

    # Full learn output
    c.print()
    c.print(f"  [bold white]{tool['tool']}[/] — {tool['description']}")
    c.print(f"  [dim]{'─' * 40}[/]")

    if tool.get("when_to_use"):
        c.print(f"  {tool['when_to_use']}\n")

    c.print("  [bold]commands[/]")
    for cmd in tool['commands']:
        c.print(f"    [cyan]{cmd['cmd']}[/]")
        c.print(f"    [dim]{cmd['meaning']}[/]\n" if cmd != tool['commands'][-1] else f"    [dim]{cmd['meaning']}[/]")

    if tool.get("filters"):
        c.print()
        c.print("  [bold]useful filters[/]")
        for f in tool['filters']:
            c.print(f"    [cyan]{f['filter']}[/]")
            c.print(f"    [dim]{f['meaning']}[/]")

    if tool.get("common_modes"):
        c.print()
        c.print("  [bold]common hash modes[/]")
        for m in tool['common_modes']:
            c.print(f"    [cyan]-m {m['mode']}[/]  [dim]{m['type']}[/]")

    if tool.get("key_concepts"):
        c.print()
        c.print("  [bold]key concepts[/]")
        for k in tool['key_concepts']:
            c.print(f"    [cyan]{k['term']}[/]  [dim]{k['meaning']}[/]")

    if tool.get("workflow"):
        c.print()
        c.print("  [bold]workflow[/]")
        for step in tool['workflow']:
            c.print(f"    [cyan]{step['step']}.[/]  {step['description']}")

    if tool.get("wordlists"):
        c.print()
        c.print("  [bold]wordlists[/]")
        for w in tool['wordlists']:
            c.print(f"    [cyan]{w['path']}[/]")
            c.print(f"    [dim]{w['meaning']}[/]")

    if tool.get("supported_services"):
        c.print()
        services = "  ·  ".join(tool['supported_services'])
        c.print(f"  [bold]supported services[/]  [dim]{services}[/]")

    if tool.get("after"):
        c.print()
        c.print("  [bold]what to do after[/]")
        for t in tool['after']:
            c.print(f"    gyra learn {t}")

    c.print()

def show_flag(tool, flag, brief):
    match = None
    for cmd in tool['commands']:
        if cmd.get("flag") and cmd["flag"].lower() == flag.lower():
            match = cmd
            break

    if not match:
        c.print(f"\n  [red]no entry for flag:[/] {flag} in {tool['tool']}")
        c.print(f"  [dim]try:[/] gyra learn {tool['tool']}\n")
        return

    if brief:
        c.print(f"\n  [bold white]{tool['tool']} {flag}[/] — {match['flag_meaning']}")
        c.print(f"  use: [cyan]{match['cmd']}[/]\n")
        return

    c.print()
    c.print(f"  [bold white]{tool['tool']} {flag}[/] — {match['flag_meaning']}")
    c.print(f"  [dim]{'─' * 40}[/]")
    c.print(f"  {match['meaning']}\n")
    c.print(f"  [bold]example[/]")
    c.print(f"    [cyan]{match['cmd']}[/]\n")
    if match.get("combine_with"):
        c.print("  [bold]combine with[/]")
        for combo in match["combine_with"]:
            c.print(f"    [cyan]{combo['cmd']}[/]  [dim]{combo['meaning']}[/]")
        c.print()
