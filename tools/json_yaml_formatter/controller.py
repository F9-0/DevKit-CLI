import json
import yaml
import os
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()

def format_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        formatted_str = json.dumps(data, indent=4, sort_keys=True)
        syntax = Syntax(formatted_str, "json", theme="default", line_numbers=True)
        console.print(syntax)
    except json.JSONDecodeError as e:
        console.print(f"[bold red]Error: Invalid JSON format. {e}[/bold red]")
    except IOError as e:
        console.print(f"[bold red]Error reading file: {e}[/bold red]")

def format_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        
        formatted_str = yaml.dump(data, indent=4, default_flow_style=False)
        syntax = Syntax(formatted_str, "yaml", theme="default", line_numbers=True)
        console.print(syntax)
    except yaml.YAMLError as e:
        console.print(f"[bold red]Error: Invalid YAML format. {e}[/bold red]")
    except IOError as e:
        console.print(f"[bold red]Error reading file: {e}[/bold red]")

def run():
    console.print(Panel.fit(
        "[bold cyan]JSON & YAML Formatter[/bold cyan]\n\nValidates and pretty-prints a JSON or YAML file.",
        title="Tool Information"
    ))
    
    file_path = console.input("[bold yellow]Enter the path to the JSON or YAML file: [/bold yellow]").strip()

    if not os.path.isfile(file_path):
        console.print(f"\n[bold red]Error: File not found at '{file_path}'[/bold red]")
        return
        
    file_extension = os.path.splitext(file_path)[1].lower()

    console.print("\n[bold green]-- Formatted Output --[/bold green]")
    if file_extension in ['.json']:
        format_json(file_path)
    elif file_extension in ['.yaml', '.yml']:
        format_yaml(file_path)
    else:
        console.print(f"[bold red]Error: Unsupported file type '{file_extension}'. Please use .json, .yaml, or .yml.[/bold red]")