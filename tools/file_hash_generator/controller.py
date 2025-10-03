import hashlib
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress

# Initialize Rich Console
console = Console()

def calculate_hashes(file_path):
    """
    Calculates MD5, SHA-1, and SHA-256 hashes for a given file,
    displaying a progress bar for large files.
    """
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()

    file_size = os.path.getsize(file_path)
    chunk_size = 8192  # Read in 8KB chunks

    try:
        with Progress(console=console, transient=True) as progress:
            task = progress.add_task("[cyan]Calculating Hashes...", total=file_size)
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    sha1.update(chunk)
                    sha256.update(chunk)
                    md5.update(chunk)
                    progress.update(task, advance=len(chunk))
        
        return {
            "MD5": md5.hexdigest(),
            "SHA-1": sha1.hexdigest(),
            "SHA-256": sha256.hexdigest(),
        }

    except IOError as e:
        console.print(f"[bold red]Error reading file: {e}[/bold red]")
        return None

def run():
    """Main function to run the File Hash Generator tool."""
    console.print(Panel.fit(
        "[bold cyan]File Hash Generator[/bold cyan]\n\nCalculates MD5, SHA-1, and SHA-256 for a specified file.",
        title="Tool Information"
    ))

    file_path = console.input("[bold yellow]Enter the full path to the file: [/bold yellow]").strip()

    # --- Input Validation ---
    if not os.path.exists(file_path):
        console.print(f"\n[bold red]Error: File not found at '{file_path}'[/bold red]")
        return
    
    if not os.path.isfile(file_path):
        console.print(f"\n[bold red]Error: The path '{file_path}' points to a directory, not a file.[/bold red]")
        return

    console.print(f"\n[green]Processing file:[/] [cyan]{os.path.basename(file_path)}[/cyan]")
    
    # --- Hash Calculation ---
    hashes = calculate_hashes(file_path)

    # --- Display Results ---
    if hashes:
        table = Table(title="[bold]File Hashes[/bold]", show_header=True, header_style="bold magenta")
        table.add_column("Algorithm", style="dim", width=12)
        table.add_column("Hash Value", style="bold green")

        for algo, hash_value in hashes.items():
            table.add_row(algo, hash_value)
            
        console.print("\n")
        console.print(table)