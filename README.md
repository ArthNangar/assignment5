# Modular Calculator with Advanced Design Patterns and pandas (REPL)

Advanced modular calculator application using Python that integrates multiple design patterns,
persistent data management via pandas, and full test automation with GitHub Actions.

## Features

- REPL interface with commands: `help`,
 `add`, `sub`, `mul`,`div`, `pow`, `root`, `history`, `undo`, `redo`, `clear`, `save`, `load`, `exit`
- Arithmetic operations: add, sub, mul, div, pow, root
- **Design patterns**:
  - **Strategy**: interchangeable operation strategies
  - **Factory**: operation factory by user input
  - **Observer**: history events
  - **Memento**: full undo/redo
  - **Facade**: CalculatorFacade hides subsystems behind simple methods
- **pandas** for history (CSV persistence with auto-load & auto-save)
- **dotenv** config in `.env` w/ validation (see `app/calculator_config.py`)
- **pytest** tests with parameterization.
- **Automated CI/CD** with github actions.

## Project Structure
```bash
advanced-calculator/
├── app/
│   ├── calculator_repl.py        # REPL interface
│   ├── calculation.py            # Calculation logic
│   ├── calculator_config.py      # Config management (.env)
│   ├── calculator_memento.py     # Re-exports Memento classes
│   ├── exceptions.py             # Custom exception classes
│   ├── history.py                # History management
│   ├── input_validators.py       # Input validation logic
│   ├── operations.py             # Arithmetic operations
│   └── __init__.py
├── tests/                        # All unit & parameterized tests
│   ├── test_calculations.py
│   ├── test_calculator_repl.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   └── test_operations.py
├── requirements.txt
├── pytest.ini
├── .github/workflows/python-app.yml
└── README.md

```

## Installation
Clone the repository and set up your environment:

```bash
git clone 
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

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
- `save [path]` → save history CSV
- `load [path]` → load history CSV
- `exit` → quit

## CI: GitHub Actions

Push this repo to GitHub. The workflow at `.github/workflows/python-app.yml` runs tests and fails if coverage < 90%.

## Design Highlights

```
Facade Pattern simplifies the interface between user input and backend logic.

Observer Pattern enables automatic CSV saving on every change.

Memento Pattern powers undo/redo using state snapshots.

Strategy Pattern makes each operation modular and easily extendable.

Factory Pattern creates operations dynamically from user commands.

Pandas Integration provides powerful, persistent data management.
```

##  License

MIT License – see LICENSE
 for details.

## 👤 Author

Arth Nangar

Date: 10/06/2025