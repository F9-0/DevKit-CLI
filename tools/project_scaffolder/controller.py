import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

TEMPLATES = {
    "1": {
        "name": "Basic Python CLI Application",
        "dirs": ["src", "tests"],
        "files": {
            ".gitignore": "# Python standard\n__pycache__/\nvenv/\n.env",
            "README.md": "# Project Title\n\nProject description.",
            "requirements.txt": "rich\n",
            "src/main.py": "def main():\n    print(\"Hello, World!\")\n\nif __name__ == \"__main__\":\n    main()\n"
        }
    },
    "2": {
        "name": "Simple Flask Web Application",
        "dirs": ["app/static", "app/templates"],
        "files": {
            ".gitignore": "# Python standard\n__pycache__/\nvenv/\n.env",
            "README.md": "# Flask Project\n\nA simple Flask web application.",
            "requirements.txt": "Flask\n",
            "app/main.py": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return \"Hello, Flask!\"\n\nif __name__ == '__main__':\n    app.run(debug=True)\n",
            "app/templates/index.html": "<!DOCTYPE html><html><head><title>Flask App</title></head><body><h1>Welcome!</h1></body></html>"
        }
    }
}

def run():
    console.print(Panel.fit(
        "[bold cyan]Project Scaffolder[/bold cyan]\n\nCreates a new project structure from predefined templates.",
        title="Tool Information"
    ))

    # --- NEW: Improved Input Handling ---
    project_path_input = console.input("[bold yellow]Enter project name or full path: [/bold yellow]").strip()
    if not project_path_input:
        console.print("[bold red]Error: Project name or path cannot be empty.[/bold red]")
        return
        
    # --- NEW: Smarter Path Resolution ---
    # This creates the correct absolute path whether the user input is a name or a full path.
    target_path = os.path.abspath(project_path_input)
        
    if os.path.exists(target_path):
        console.print(f"[bold red]Error: The path '{target_path}' already exists.[/bold red]")
        console.print("Please choose a different name or location.")
        return

    console.print("\n[bold]Available Templates:[/bold]")
    for key, value in TEMPLATES.items():
        console.print(f"  [cyan]{key}[/cyan] - {value['name']}")
        
    template_choice = Prompt.ask("\nSelect a template", choices=list(TEMPLATES.keys()))
    if not template_choice:
        console.print("[yellow]No template selected. Operation cancelled.[/yellow]")
        return
        
    template = TEMPLATES[template_choice]
    
    try:
        project_name = os.path.basename(target_path)
        with console.status(f"[bold green]Scaffolding project '{project_name}' at '{target_path}'...[/bold green]"):
            # Create root directory using the resolved absolute path
            os.makedirs(target_path)
            console.log(f"Created root directory: [cyan]{target_path}[/cyan]")

            # Create subdirectories inside the target path
            for d in template["dirs"]:
                dir_path = os.path.join(target_path, d)
                os.makedirs(dir_path)
                console.log(f"Created directory: [cyan]{dir_path}[/cyan]")

            # Create files with content inside the target path
            for file_path, content in template["files"].items():
                full_path = os.path.join(target_path, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                console.log(f"Created file: [cyan]{full_path}[/cyan]")
                
        console.print(f"\n[bold green]Project '{project_name}' scaffolded successfully![/bold green]")
    except OSError as e:
        console.print(f"[bold red]An OS error occurred during file creation: {e}[/bold red]")