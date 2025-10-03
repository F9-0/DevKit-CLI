import os
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Initialize Rich Console
console = Console()

# Directories and files to ignore
IGNORE_LIST = {
    "__pycache__",
    ".git",
    ".vscode",
    ".idea",
    "node_modules",
    "venv",
    ".venv"
}

def add_items_to_tree(directory: str, tree: Tree):
    """Recursively adds files and directories to the rich Tree."""
    try:
        items = sorted(os.listdir(directory))
        for item in items:
            if item in IGNORE_LIST:
                continue
            
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                # It's a directory, add a new branch and recurse
                branch = tree.add(f" [bold magenta]{item}[/bold magenta]")
                add_items_to_tree(item_path, branch)
            else:
                # It's a file
                tree.add(f" [cyan]{item}[/cyan]")

    except PermissionError:
        tree.add("[bold red]Permission Denied[/bold red]")
    except Exception as e:
        tree.add(f"[bold red]Error: {e}[/bold red]")


def run():
    """Main function to run the Directory Tree Generator tool."""
    console.print(Panel.fit(
        "[bold cyan]Directory Tree Generator[/bold cyan]\n\nVisualizes the structure of a directory.",
        title="Tool Information"
    ))

    path = console.input(
        "[bold yellow]Enter the directory path (or press Enter for current directory): [/bold yellow]"
    ).strip()

    # Default to current directory if no input is given
    if not path:
        path = "."

    # --- Input Validation ---
    if not os.path.exists(path):
        console.print(f"\n[bold red]Error: Path not found at '{path}'[/bold red]")
        return
    
    if not os.path.isdir(path):
        console.print(f"\n[bold red]Error: The path '{path}' is not a directory.[/bold red]")
        return
        
    console.print("\n")
    
    # --- Generate Tree ---
    tree_title = f" Tree for '{os.path.abspath(path)}'"
    tree = Tree(tree_title, guide_style="bold bright_blue")
    add_items_to_tree(path, tree)
    
    # --- Print Tree ---
    console.print(tree)