import subprocess
import re
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def is_git_repository():
    """Check if the current directory is a git repository."""
    return subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True).stdout.strip() == 'true'

def get_formatted_log():
    """Returns a nicely formatted git log."""
    cmd = [
        'git', 'log', '--graph',
        "--pretty=format:%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset",
        '--abbrev-commit', '-15' # Limit to last 15 commits
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout

def clean_merged_branches():
    """Identifies and offers to delete local branches that have been merged into the current branch."""
    try:
        # Get current branch
        current_branch = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
        
        # Get merged branches
        merged_branches_raw = subprocess.run(['git', 'branch', '--merged'], capture_output=True, text=True, check=True).stdout
        
        branches_to_delete = []
        for branch in merged_branches_raw.splitlines():
            branch_name = branch.strip()
            # Don't delete the current branch or protected branches like main/master
            if branch_name.startswith('*'):
                continue
            if branch_name in ['main', 'master', 'develop']:
                continue
            branches_to_delete.append(branch_name)

        if not branches_to_delete:
            console.print("[green]No local merged branches to clean up.[/green]")
            return

        console.print("[yellow]The following local branches have been merged and can be deleted:[/yellow]")
        for branch in branches_to_delete:
            console.print(f"- {branch}")
        
        if console.confirm("\n[bold]Do you want to delete these branches?[/bold]", default=False):
            for branch in branches_to_delete:
                subprocess.run(['git', 'branch', '-d', branch], check=True)
                console.print(f"Deleted branch [red]{branch}[/red]")
            console.print("\n[bold green]Cleanup complete.[/bold green]")
        else:
            console.print("Cleanup cancelled.")

    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Git Error: {e.stderr}[/bold red]")

def run():
    console.print(Panel.fit(
        "[bold cyan]Git Helper[/bold cyan]\n\nProvides shortcuts for common Git operations.",
        title="Tool Information"
    ))

    if not is_git_repository():
        console.print("[bold red]Error: Not a Git repository.[/bold red]")
        console.print("Please run this tool from within a project managed by Git.")
        return

    menu = {
        "1": "View Formatted Log (last 15 commits)",
        "2": "Clean Up Merged Local Branches",
    }
    
    console.print("\n[bold]Select a Git operation:[/bold]")
    for key, value in menu.items():
        console.print(f"  [cyan]{key}[/cyan] - {value}")
        
    choice = Prompt.ask("\nChoose an option", choices=menu.keys())

    if choice == "1":
        try:
            log_output = get_formatted_log()
            console.print("\n[bold green]-- Git Log --[/bold green]")
            console.print(log_output)
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Could not retrieve git log: {e.stderr}[/bold red]")
            
    elif choice == "2":
        clean_merged_branches()