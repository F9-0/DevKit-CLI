import subprocess
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.print(Panel.fit(
        "[bold cyan]Dependency Analyzer[/bold cyan]\n\nVisualizes the project's dependency tree from 'requirements.txt'.",
        title="Tool Information"
    ))

    req_file = "requirements.txt"

    if not os.path.isfile(req_file):
        console.print(f"\n[bold red]Error: '{req_file}' not found in the current directory.[/bold red]")
        return
        
    try:
        with console.status("[bold green]Analyzing dependencies...[/bold green]"):
            # Using --from-requirements to be explicit
            result = subprocess.run(
                ['pipdeptree', '--from-requirements', req_file],
                capture_output=True,
                text=True,
                check=True
            )
        
        console.print("\n[bold green]-- Dependency Tree --[/bold green]")
        console.print(Panel(result.stdout or "No dependencies found.", title=f"Dependencies from {req_file}", border_style="green"))

    except FileNotFoundError:
        console.print("[bold red]Error: 'pipdeptree' command not found.[/bold red]")
        console.print("Please ensure the virtual environment is active and 'pipdeptree' is installed.")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]An error occurred while running pipdeptree:[/bold red]")
        console.print(Panel(e.stderr or "No error output.", title="Error Details", border_style="red"))