# main.py

import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Import all tool controllers
# Note: Ensure all these files exist as per our previous setup
from tools import (
    source_code_review, project_scaffolder, jwt_debugger,
    api_requester, json_yaml_formatter, file_hash_generator,
    base64_encoder_decoder, regex_tester, directory_tree_generator,
    dependency_analyzer, git_helper, secret_scanner
)

console = Console()

# --- Interactive Menu Logic (from our old version) ---

TOOLS_MAP = {
    "1": {"name": "Source Code Review", "controller": source_code_review},
    "2": {"name": "Project Scaffolder", "controller": project_scaffolder},
    "3": {"name": "JWT Debugger", "controller": jwt_debugger},
    "4": {"name": "API Requester", "controller": api_requester},
    "5": {"name": "JSON & YAML Formatter", "controller": json_yaml_formatter},
    "6": {"name": "File Hash Generator", "controller": file_hash_generator},
    "7": {"name": "Base64 Encoder/Decoder", "controller": base64_encoder_decoder},
    "8": {"name": "Regex Tester", "controller": regex_tester},
    "9": {"name": "Directory Tree Generator", "controller": directory_tree_generator},
    "10": {"name": "Dependency Analyzer", "controller": dependency_analyzer},
    "11": {"name": "Git Helper", "controller": git_helper},
    "12": {"name": "Secret Scanner", "controller": secret_scanner},
}

def display_interactive_banner():
    """Displays the beautiful banner for the interactive mode."""
    console.print(Panel("""
[bold magenta]██████╗ ███████╗██╗   ██╗██╗  ██╗██╗████████╗     ██████╗██╗      ██╗[/bold magenta]
[bold magenta]██╔══██╗██╔════╝██║   ██║██║ ██╔╝██║╚══██╔══╝    ██╔════╝██║      ██║[/bold magenta]
[bold magenta]██║  ██║█████╗  ██║   ██║█████╔╝ ██║   ██║█████╗██║      ██║      ██║[/bold magenta]
[bold magenta]██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═██╗ ██║   ██║╚════╝██║      ██║      ██║[/bold magenta]
[bold magenta]██████╔╝███████╗ ╚████╔╝ ██║  ██╗██║   ██║      ╚██████╗ ███████╗ ██║[/bold magenta]
[bold magenta]╚═════╝ ╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝   ╚═╝       ╚═════╝ ╚══════╝ ╚═╝[/bold magenta]
[cyan]A Professional Suite of Power Tools for Developers[/cyan]
    """, title="[bold green]Welcome to DevKit CLI[/bold green]", border_style="green", expand=False))

def run_interactive_menu():
    """The main loop for the interactive menu mode."""
    while True:
        display_interactive_banner()
        console.print("\n[bold yellow]Select a tool to run:[/bold yellow]")
        for key, value in TOOLS_MAP.items():
            console.print(f"  [bold cyan]{key:>2}[/bold cyan] - {value['name']}")
        console.print(f"  [bold red] 0[/bold red] - Exit\n")
        
        choice = Prompt.ask("[bold]Enter the tool number[/bold]", default="0")

        if choice == "0":
            console.print("[bold green]Goodbye![/bold green]")
            break

        selected_tool = TOOLS_MAP.get(choice)
        if selected_tool:
            console.rule(f"[bold green]Launching: {selected_tool['name']}[/bold green]")
            try:
                selected_tool['controller'].run()
            except Exception as e:
                console.print(f"[bold red]An unexpected error occurred in the tool:[/bold red]\n{e}")
            
            console.print("\nPress Enter to return to the main menu...")
            input()
        else:
            console.print("[bold red]Invalid choice. Press Enter to continue...[/bold red]")
            input()


# --- Click CLI Framework Logic ---

@click.group(invoke_without_command=True)
@click.pass_context
def devkit(ctx):
    """
    DevKit CLI: A Professional Suite of Power Tools for Developers.
    If no command is specified, runs in interactive mode.
    """
    if ctx.invoked_subcommand is None:
        # If no command was specified, run our beautiful interactive menu
        run_interactive_menu()

# Define a simple command as an example of direct execution
@devkit.command()
@click.argument('filepath', type=click.Path(exists=True, dir_okay=False))
def hash(filepath):
    """Calculates hashes for a given file."""
    # This requires refactoring the controller to accept an argument.
    # For now, this shows the direct command structure.
    console.print(f"[bold]Running Hash Generator for:[/] [cyan]{filepath}[/cyan]")
    file_hash_generator.run() 

if __name__ == '__main__':
    devkit()