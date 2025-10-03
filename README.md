<img alt="Python" src="https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python&logoColor=white">
<img alt="Rich" src="https://img.shields.io/badge/CLI--rich-2496ED?style=flat&logo=python&logoColor=white&labelColor=black">
<img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
<img alt="Code Quality" src="https://www.codefactor.io/repository/github/your_username/source-code-review/badge">

<div align="center">

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/CLI--rich-2496ED?style=flat&logo=python&logoColor=white&labelColor=black)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Code Quality](https://www.codefactor.io/repository/github/your_username/source-code-review/badge)

</div>

A powerful command-line tool to analyze source code for quality, performance, and style issues, presenting the results in a clean, human-readable format.

---

أداة سطر أوامر قوية لتحليل الشيفرة المصدرية، والكشف عن مشكلات الجودة، الأداء، ونمط الكتابة، مع عرض النتائج بشكل منظم وسهل القراءة.

---

###  Demo

*(Here you can add a GIF or screenshot demonstrating the tool's output.)*

![Demo Placeholder](https://user-images.githubusercontent.com/10933930/224762512-b1399b24-da1a-45c1-8f5b-1e7c3311f692.png)

### ✨ Key Features

-   **Comprehensive Analysis**: Checks for common code smells, potential bugs, and anti-patterns.
-   **Performance Profiling**: Identifies performance bottlenecks and suggests optimizations.
-   **Style Enforcement**: Ensures code conforms to standard style guides (e.g., PEP 8).
-   **Rich & Readable Output**: Uses tables, syntax highlighting, and progress bars for a superior user experience.
-   **Configurable**: Easily configure rules and analysis parameters.

### ⚙️ Installation

You can install `Source-Code-Review` by cloning this repository and installing the dependencies. It is highly recommended to use a virtual environment.

#### On Linux / macOS

```bash
# 1. Clone the repository
git clone [https://github.com/your_username/source-code-review.git](https://github.com/your_username/source-code-review.git)
cd source-code-review

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install the required packages
pip install -r requirements.txt
```

#### On Windows

```powershell
# 1. Clone the repository
git clone [https://github.com/your_username/source-code-review.git](https://github.com/your_username/source-code-review.git)
cd source-code-review

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install the required packages
pip install -r requirements.txt
```

### 🚀 Usage

Once installed, you can run the tool from the command line.

#### Analyze a single file:

```bash
python main.py path/to/your/file.py
```

#### Analyze an entire directory:

The tool will recursively scan the directory for supported file types.

```bash
python main.py path/to/your/project/
```

#### Analyze with specific checks (e.g., performance only):

```bash
python main.py path/to/your/project/ --check performance
```

#### Export report to a file:

```bash
python main.py path/to/your/project/ --output report.json
```

### 🤝 Contributing

Contributions are welcome! Whether it's a bug report, a new feature, or a documentation improvement, please feel free to open an issue or submit a pull request.

Please read our `CONTRIBUTING.md` guide for details on our code of conduct and the process for submitting pull requests.

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.