import jwt
import json
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()

def run():
    console.print(Panel.fit(
        "[bold cyan]JWT Debugger[/bold cyan]\n\nDecodes a JSON Web Token to inspect its header and payload.",
        title="Tool Information"
    ))
    
    token = console.input("[bold yellow]Enter the JWT to decode: [/bold yellow]").strip()

    if not token:
        console.print("[bold red]Error: No token provided.[/bold red]")
        return
    
    try:
        # We decode without verification to inspect contents
        header = jwt.get_unverified_header(token)
        payload = jwt.decode(token, options={"verify_signature": False, "verify_aud": False})

        header_str = json.dumps(header, indent=4)
        payload_str = json.dumps(payload, indent=4)
        
        console.print("\n[bold green]-- JWT Header --[/bold green]")
        console.print(Syntax(header_str, "json", theme="monokai", line_numbers=True))
        
        console.print("\n[bold green]-- JWT Payload --[/bold green]")
        console.print(Syntax(payload_str, "json", theme="monokai", line_numbers=True))

    except jwt.exceptions.DecodeError as e:
        console.print(f"[bold red]Error: Invalid token format. Could not decode JWT.[/bold red]")
        console.print(f"Details: {e}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")