import subprocess
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.print(Panel.fit(
        "[bold cyan]Source Code Review[/bold cyan]\n\nAnalyzes a Python file for style and quality issues using Pylint.",
        title="Tool Information"
    ))

    file_path = console.input("[bold yellow]Enter the path to the Python file to analyze: [/bold yellow]").strip()

    if not os.path.isfile(file_path):
        console.print(f"\n[bold red]Error: File not found at '{file_path}'[/bold red]")
        return
        
    if not file_path.endswith('.py'):
        console.print(f"\n[bold red]Error: This tool only analyzes Python (.py) files.[/bold red]")
        return
        
    try:
        with console.status("[bold green]Running Pylint analysis...[/bold green]"):
            result = subprocess.run(
                ['pylint', file_path],
                capture_output=True,
                text=True,
                check=False # Do not raise exception on non-zero exit code
            )
        
        console.print("\n[bold green]-- Pylint Analysis Report --[/bold green]")
        if result.stdout:
            console.print(Panel(result.stdout, title="Report", border_style="green"))
        else:
            console.print("[yellow]No issues found by Pylint, or Pylint produced no output.[/yellow]")

        if result.stderr:
            console.print("\n[bold red]-- Pylint Errors --[/bold red]")
            console.print(Panel(result.stderr, title="Errors", border_style="red"))

    except FileNotFoundError:
        console.print("[bold red]Error: 'pylint' command not found.[/bold red]")
        console.print("Please ensure Pylint is installed and in your system's PATH.")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")