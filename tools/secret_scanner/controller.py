import os
import re
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

SECRET_PATTERNS = {
    "API Key": re.compile(r'api[_-]?key[\s_]*[=:]\s*[\'"]([a-zA-Z0-9_.-]{16,})[\'"]'),
    "AWS Access Key": re.compile(r'(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])'),
    "GitHub Token": re.compile(r'ghp_[a-zA-Z0-9]{36}'),
    "Private Key": re.compile(r'-----BEGIN ((RSA|OPENSSH) )?PRIVATE KEY-----'),
}

IGNORE_EXTENSIONS = ['.log', '.lock', '.svg', '.png', '.jpg', '.jpeg', '.gif']
IGNORE_DIRS = {'/.git', '/.venv', '/venv', '/node_modules', '/__pycache__'}

def scan_file(filepath, findings):
    """Scans a single file for secrets."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for secret_type, pattern in SECRET_PATTERNS.items():
                    if pattern.search(line):
                        findings.append((secret_type, filepath, line_num, line.strip()))
    except Exception:
        pass # Ignore files that cannot be read

def run():
    console.print(Panel.fit(
        "[bold cyan]Secret Scanner[/bold cyan]\n\nScans a directory for hardcoded secrets.",
        title="Tool Information"
    ))
    
    target_dir = console.input("[bold yellow]Enter directory path to scan (default: current): [/bold yellow]").strip() or "."

    if not os.path.isdir(target_dir):
        console.print(f"[bold red]Error: '{target_dir}' is not a valid directory.[/bold red]")
        return
        
    findings = []
    with console.status("[bold green]Scanning...[/bold green]"):
        for root, _, files in os.walk(target_dir):
            if any(ignored_dir in root for ignored_dir in IGNORE_DIRS):
                continue
            for file in files:
                if not any(file.endswith(ext) for ext in IGNORE_EXTENSIONS):
                    scan_file(os.path.join(root, file), findings)

    if not findings:
        console.print("\n[bold green]No potential secrets found.[/bold green]")
        return

    console.print("\n[bold red]Potential Secrets Found![/bold red]")
    table = Table(title="Scan Results")
    table.add_column("Type", style="cyan")
    table.add_column("File Path", style="yellow")
    table.add_column("Line", style="dim")
    table.add_column("Content", style="red")

    for f_type, f_path, f_line, f_content in findings:
        table.add_row(f_type, f_path, str(f_line), f_content)
        
    console.print(table)