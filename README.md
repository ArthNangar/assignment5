# Advanced Modular Calculator (REPL)

A sophisticated, modular calculator application using Python that integrates multiple design patterns,
persistent data management via **pandas**, and full test automation with **GitHub Actions**.

## Features

- REPL interface with commands: `help`, `add/sub/mul/div/pow/root`, `history`, `undo`, `redo`, `clear`, `save`, `load`, `exit`
- Arithmetic operations: add, sub, mul, div, pow, root
- **Design patterns**:
  - **Strategy**: interchangeable operation strategies
  - **Factory**: operation factory by user input
  - **Observer**: history events (auto-save/logging)
  - **Memento**: full undo/redo (history & cursor state)
  - **Facade**: `CalculatorFacade` hides subsystems behind simple methods
- **pandas** for history (CSV persistence with auto-load & auto-save)
- **dotenv** config in `.env` w/ validation (see `app/calculator_config.py`)
- DRY, modular, well-documented
- **pytest** tests with parameterization and 100% coverage in CI (uses `# pragma: no cover` where appropriate)

## Quickstart

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

# (Optional) Create a .env to override defaults
# HISTORY_FILE=history.csv
# AUTOSAVE=true

# Run tests + coverage
pytest --cov=app tests/

# Start REPL
python -m app.calculator_repl
```

## Commands

- `add 1 2`, `sub 3 1`, `mul 2 4`, `div 4 2`, `pow 2 3`, `root 9 2`
- `history` → show saved rows
- `undo` / `redo` → revert/restore last calculation
- `clear` → clear in-memory history
- `save [path]` → save history CSV (default from config)
- `load [path]` → load history CSV
- `exit` → quit

## CI: GitHub Actions

Push this repo to GitHub. The workflow at `.github/workflows/python-app.yml` runs tests and fails if coverage < 90%.
