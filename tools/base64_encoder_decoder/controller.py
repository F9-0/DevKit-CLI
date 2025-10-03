import base64
from binascii import Error as BinasciiError
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Initialize Rich Console
console = Console()

def run():
    """Main function to run the Base64 Encoder/Decoder tool."""
    console.print(Panel.fit(
        "[bold cyan]Base64 Encoder/Decoder[/bold cyan]\n\nEncodes a string to Base64 or decodes a Base64 string.",
        title="Tool Information"
    ))

    # --- Let user choose the operation ---
    operation = Prompt.ask(
        "Choose an operation",
        choices=["encode", "decode"],
        default="encode"
    )

    if operation == "encode":
        # --- ENCODING LOGIC ---
        input_text = console.input("[yellow]Enter the string to encode: [/yellow]")
        
        try:
            # String must be encoded to bytes before base64 encoding
            encoded_bytes = base64.b64encode(input_text.encode('utf-8'))
            # Decode bytes back to string for printing
            encoded_string = encoded_bytes.decode('utf-8')
            
            console.print("\n[bold green]-- Encoded Result --[/bold green]")
            console.print(Panel(encoded_string, style="green"))

        except Exception as e:
            console.print(f"[bold red]An error occurred during encoding: {e}[/bold red]")

    elif operation == "decode":
        # --- DECODING LOGIC ---
        input_text = console.input("[yellow]Enter the Base64 string to decode: [/yellow]")

        try:
            # String must be encoded to bytes before base64 decoding
            decoded_bytes = base64.b64decode(input_text.encode('utf-8'))
            # Decode bytes back to string for printing
            decoded_string = decoded_bytes.decode('utf-8')

            console.print("\n[bold green]-- Decoded Result --[/bold green]")
            console.print(Panel(decoded_string, style="green"))

        except BinasciiError:
            console.print("\n[bold red]Error: Invalid Base64 string.[/bold red]")
            console.print("The input string contains non-Base64 characters or is improperly padded.")
        except Exception as e:
            console.print(f"[bold red]An error occurred during decoding: {e}[/bold red]")