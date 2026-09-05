# Employee Performance Evaluator(NOT DONE, STILL IN TESTING)

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

## Preview
<p align="center">
<img width="644" height="599" alt="image" src="https://github.com/user-attachments/assets/806bbc8b-3d78-428f-9ecf-6e254a1d469b" />
<img width="645" height="601" alt="image" src="https://github.com/user-attachments/assets/513bad53-0170-4d34-8132-8705ae201e17" />
<img width="644" height="598" alt="image" src="https://github.com/user-attachments/assets/bb120465-c220-42f1-8e74-0fc2b6839a44" />
<img width="645" height="599" alt="image" src="https://github.com/user-attachments/assets/95c5dde8-3a66-421a-bfff-44e19eb704cf" />
<img width="646" height="600" alt="image" src="https://github.com/user-attachments/assets/f5165737-8ceb-43fe-8e0f-23650619b8cc" />
<img width="643" height="601" alt="image" src="https://github.com/user-attachments/assets/651b1fd4-d88e-499e-9092-8b6d9632a70c" />
</p>

