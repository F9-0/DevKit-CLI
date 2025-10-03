import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

console = Console()

def run():
    console.print(Panel.fit(
        "[bold cyan]API Requester[/bold cyan]\n\nSends an HTTP request to a specified URL and displays the response.",
        title="Tool Information"
    ))

    method = Prompt.ask("Select HTTP Method", choices=["GET", "POST", "PUT", "DELETE"], default="GET").upper()
    url = console.input("[bold yellow]Enter the full URL: [/bold yellow]").strip()
    
    if not url:
        console.print("[bold red]Error: URL cannot be empty.[/bold red]")
        return
        
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    headers, payload = {}, None

    if console.confirm("Add custom headers?"):
        console.print("Enter headers as key=value. Press Enter on an empty line to finish.")
        while True:
            header_line = console.input("  [cyan]Header > [/cyan]")
            if not header_line: break
            if '=' in header_line:
                key, value = header_line.split('=', 1)
                headers[key.strip()] = value.strip()

    if method in ["POST", "PUT"]:
        if console.confirm("Add a JSON body?"):
            console.print("Enter the JSON body. Press Ctrl+D (Linux/Mac) or Ctrl+Z+Enter (Windows) when done.")
            json_lines = []
            try:
                while True: json_lines.append(input())
            except EOFError: pass
            
            try:
                payload = json.loads("\n".join(json_lines))
            except json.JSONDecodeError as e:
                console.print(f"[bold red]Invalid JSON body: {e}[/bold red]")
                return

    try:
        with console.status("[bold green]Sending request...[/bold green]", spinner="dots"):
            response = requests.request(method, url, headers=headers, json=payload, timeout=15)

        console.print(f"\n[bold green]-- Response --[/bold green]")
        console.print(f"Status: [bold {'green' if response.ok else 'red'}]{response.status_code} {response.reason}[/bold {'green' if response.ok else 'red'}]")
        
        try:
            response_json = response.json()
            console.print(Syntax(json.dumps(response_json, indent=4), "json", theme="monokai", line_numbers=True))
        except json.JSONDecodeError:
            console.print(Panel(response.text or "[No content]", title="Response Body (Text)"))
            
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]An error occurred during the request: {e}[/bold red]")