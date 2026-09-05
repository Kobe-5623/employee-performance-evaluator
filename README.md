# Employee Performance Evaluator(NOT SURE IF DONE)

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
├── clips/
│   ├── templates.clp
│   ├── questions.clp
│   └── rules.clp
├── src/
│   └── expertsystem/
│       ├── __init__.py
│       └── main.py
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

## Questions I asked AI to get the info I need for this expert system
* What do you usually look at when deciding if an employee is doing a good job?
* What areas of an employee’s performance are the most important to check?
* What kind of behavior thqt would show that an employee is performing well?
* What questions would you normally ask when evaluating an employee?
* How would you normally rate performance of a employee?
* How would you combine the answers to get an overall performance score?
* Are some areas in performance more important than others? If so which ones?
* How would you decide whether an employee is excellent, satisfactory, or needs improvement?
* What am I even doing?

## Infos I got and used
Areas of Performance and Weights I got based on its importance:
> * Work Performance - 30%
> * Communication & Teamwork - 20%
> * Compliance & Accountability - 15%
> * Problem Solving & Adaptability - 15%
> * Quality & Professionalism - 20%

Questions I can ask to evaluate a employee's perforamance in general:
> 1. How effectively does the employee perform the main duties and responsibilities required by their position?
> 2. How well does the employee organize and complete assigned work accurately and within the expected time?
> 3. How effectively does the employee communicate information, ideas, and concerns with coworkers and other people they work with?
> 4. How well does the employee cooperate with coworkers and contribute to completing shared tasks and team responsibilities?
> 5. How consistently does the employee follow workplace policies, procedures, instructions, and established standards when performing their duties?
> 6. How reliably does the employee take responsibility for assigned duties and ensure that their work is completed as expected?
> 7. How effectively does the employee identify problems that affect their work and take appropriate action to resolve them?
> 8. How well does the employee adjust their approach when work requirements, priorities, procedures, or situations change?
> 9. How consistently does the employee produce work that meets the expected standards for accuracy, completeness, and quality?
> 10. How professionally does the employee conduct themselves when carrying out responsibilities and interacting with others in the workplace?

Templates I need:
> * question
> * answer
> * area-score
> * overall-score
> * result

## Inference System
When the answers are submitted, the scores are asserted as answer facts. Rules will use the answers per areas then get their average, then it will assert a area-score fact, it will happenn to every areas. After that overall score are calculated based on each area's importance, then assert overall-score fact. Lastly the appropriate output to say are chosen based on overall score, such as Excellent, Very Satisfactory, Satisfactory, or Needs Improvement.

## Preview
<p align="center">
<img width="644" height="599" alt="image" src="https://github.com/user-attachments/assets/806bbc8b-3d78-428f-9ecf-6e254a1d469b" />
<img width="645" height="601" alt="image" src="https://github.com/user-attachments/assets/513bad53-0170-4d34-8132-8705ae201e17" />
<img width="644" height="598" alt="image" src="https://github.com/user-attachments/assets/bb120465-c220-42f1-8e74-0fc2b6839a44" />
<img width="645" height="599" alt="image" src="https://github.com/user-attachments/assets/95c5dde8-3a66-421a-bfff-44e19eb704cf" />
<img width="646" height="600" alt="image" src="https://github.com/user-attachments/assets/f5165737-8ceb-43fe-8e0f-23650619b8cc" />
<img width="643" height="601" alt="image" src="https://github.com/user-attachments/assets/651b1fd4-d88e-499e-9092-8b6d9632a70c" />
</p>

