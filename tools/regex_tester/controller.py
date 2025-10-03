import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def run():
    console.print(Panel.fit(
        "[bold cyan]Regex Tester[/bold cyan]\n\nInteractively test a regular expression against a body of text.",
        title="Tool Information"
    ))

    pattern_str = console.input("[bold yellow]Enter the regular expression pattern: [/bold yellow]")
    try:
        pattern = re.compile(pattern_str)
    except re.error as e:
        console.print(f"[bold red]Invalid Regex Pattern: {e}[/bold red]")
        return
        
    console.print("[yellow]Enter the text to test against. Press Ctrl+D (Linux/Mac) or Ctrl+Z+Enter (Windows) when done.[/yellow]")
    
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    test_text = "\n".join(lines)
    
    console.print("\n[bold green]-- Match Results --[/bold green]")

    matches = list(pattern.finditer(test_text))
    
    if not matches:
        console.print("[yellow]No matches found.[/yellow]")
        return

    console.print(f"Found [bold]{len(matches)}[/bold] match(es).")
    
    highlighted_text = Text()
    last_end = 0
    for match in matches:
        start, end = match.span()
        # Append the text before the match
        highlighted_text.append(test_text[last_end:start])
        # Append the matched text with a highlight style
        highlighted_text.append(test_text[start:end], style="bold on yellow")
        last_end = end
    # Append the rest of the text
    highlighted_text.append(test_text[last_end:])
    
    console.print(Panel(highlighted_text, title="Highlighted Matches", border_style="green"))