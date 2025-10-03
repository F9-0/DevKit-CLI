<div align="center">

```
██████╗ ███████╗██╗   ██╗██╗  ██╗██╗████████╗     ██████╗██╗      ██╗
██╔══██╗██╔════╝██║   ██║██║ ██╔╝██║╚══██╔══╝    ██╔════╝██║      ██║
██║  ██║█████╗  ██║   ██║█████╔╝ ██║   ██║█████╗██║      ██║      ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═██╗ ██║   ██║╚════╝██║      ██║      ██║
██████╔╝███████╗ ╚████╔╝ ██║  ██╗██║   ██║      ╚██████╗ ███████╗ ██║
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝   ╚═╝       ╚═════╝ ╚══════╝ ╚═╝
```
# DevKit CLI
**A Professional Suite of Power Tools for Developers**

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/built%20with-Click-blue)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tools](https://img.shields.io/badge/Power_Tools-12-blueviolet.svg)

</div>

**DevKit CLI** is a powerful, integrated command-line interface that brings together a suite of essential tools for modern developers. Built with Python and Click, and enhanced with Rich, it provides a beautiful and efficient way to handle complex development tasks directly from your terminal.

---

### Tools Included

This is not just a collection of utilities; it's a curated suite of power tools designed to boost productivity and streamline complex workflows.

| #  | Tool                   | Description                                                                    |
|----|--------------------------|--------------------------------------------------------------------------------|
| 1  | **Source Code Review** | Statically analyzes code for quality, performance, and style violations.         |
| 2  | **Project Scaffolder** | Instantly creates new project structures from predefined templates. |
| 3  | **JWT Debugger** | Decodes and validates JSON Web Tokens to inspect their payload and signature. |
| 4  | **API Requester** | A powerful terminal client for sending HTTP requests to APIs. |
| 5  | **JSON & YAML Formatter**| Validates and pretty-prints complex JSON or YAML files for readability.        |
| 6  | **File Hash Generator** | Computes MD5, SHA-1, and SHA-256 hashes for file integrity verification.       |
| 7  | **Base64 Encoder/Decoder**| Encodes and decodes strings or files using the Base64 scheme.                  |
| 8  | **Regex Tester** | Interactively tests and debugs regular expressions against sample text.        |
| 9  | **Directory Tree Gen** | Generates a visual, structured tree of any directory's contents.               |
| 10 | **Dependency Analyzer** | Visualizes package dependencies from a `requirements.txt` file.   |
| 11 | **Git Helper** | Provides productivity shortcuts for complex Git operations.                    |
| 12 | **Secret Scanner** | Scans directories for hardcoded secrets like API keys and private keys.        |

---

### Installation

Get up and running with DevKit CLI in a few simple steps. A virtual environment is required.

**1. Clone the Repository**
```bash
git clone [https://github.com/f9-0/DevKit-CLI.git](https://github.com/f9-0/DevKit-CLI.git)
cd DevKit-CLI
```

**2. Create and Activate Virtual Environment**
* **On Windows (PowerShell):**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
* **On macOS / Linux (Bash/Zsh):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

**3. Install the Project**
This single command installs the tool along with all its dependencies and makes the `devkit` command available in your terminal.
```bash
# The '-e' flag installs it in "editable" mode
pip install -e .
```

---

### Usage

DevKit CLI is a hybrid tool that supports both a user-friendly interactive menu and direct commands for power users and automation.

#### Interactive Mode
For a visually rich experience, simply run the main command without any arguments. This will launch the beautiful interactive menu where you can select tools by number.
```bash
devkit
```


#### Direct Command Mode
For speed and scripting, you can call any tool directly as a subcommand.

```bash
# Get a list of all available commands
devkit --help

# Example: Get the hash of a file
devkit hash ./path/to/your/file.txt

# Example: Scan a directory for secrets
devkit scan ./path/to/project

# Example: Decode a JWT
devkit jwt "your.long.token.string"
```
