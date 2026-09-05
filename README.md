# Teacher Performance Evaluator

## Setup

Open this project in **VS Code** and open:

**Terminal → New Terminal**

### 1. Install uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
````

**Linux (Bash):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal after installing uv.

### 2. Install the project dependencies

From the project folder:

```bash
uv sync
```

This installs the Python version and project dependencies listed in `pyproject.toml`.

### 3. Run the application

```bash
uv run expertsystem
```

## Project Structure

```text
ExpertSystem/
├── src/
│   └── expertsystem/
│       ├── __init__.py
│       └── main.py
├── rules/
│   └── rules.clp
├── pyproject.toml
├── uv.lock
└── README.md
```

## Dependencies

The project uses:

* Python
* CLIPSpy
* CustomTkinter
* Tkinter

Python dependencies are managed automatically by `uv`.

> On Debian/Ubuntu-based Linux systems, Tkinter may need to be installed separately:
>
> ```bash
> sudo apt install python3-tk
> ```
