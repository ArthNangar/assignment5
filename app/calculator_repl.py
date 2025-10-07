# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

from __future__ import annotations
import sys
from typing import Optional
from .calculator_config import CalculatorConfig
from .exceptions import OperationError, ValidationError, UndoRedoError, ConfigurationError
from .input_validators import parse_two_numbers
from .calculation import Calculation
from .history import History, AutoSaveObserver, Caretaker

# Facade Pattern: encapsulates config, history, observers, operations
class CalculatorFacade:
    def __init__(self, config: Optional[CalculatorConfig] = None):
        self.config = config or CalculatorConfig.from_env()
        self.history = History()
        self.caretaker = Caretaker(self.history)

        if self.config.autosave:
            self.history.attach(AutoSaveObserver(lambda: self.config.history_file))

        # Try auto-load (EAFP)
        try:
            # If file missing, ignore
            import os
            if os.path.exists(self.config.history_file):
                self.history.load_csv(self.config.history_file)
        except Exception:  # pragma: no cover - benign
            pass

    def compute(self, op: str, a: float, b: float) -> float:
        self.caretaker.snapshot()
        try:
            result = Calculation(op, a, b).execute()
            self.history.add(op, a, b, result, None)
            return result
        except OperationError as e:
            self.history.add(op, a, b, None, str(e))
            raise

    def undo(self):
        self.caretaker.undo()

    def redo(self):
        self.caretaker.redo()

    def clear(self):
        self.caretaker.snapshot()
        self.history.clear()

    def save(self, path: Optional[str] = None):
        path = path or self.config.history_file
        self.history.save_csv(path)

    def load(self, path: Optional[str] = None):
        path = path or self.config.history_file
        self.caretaker.snapshot()
        self.history.load_csv(path)

def print_help():
    print("""Commands:
          add a b
          sub a b
          mul a b
          div a b
          pow a b
          root a b
          history : To see the history of your calculations
          undo : To undo any opearation
          redo : To redo any opearation
          clear : To clear history
          save
          load
          help
          exit
""")

def main():
    try:
        calc = CalculatorFacade()
    except ConfigurationError as e:
        print(f"Config error: {e}")
        return 1

    print("Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            raw = input("> ").strip()
        except EOFError:
            print()  # newline
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()

        if cmd in {"exit", "quit"}:
            break
        elif cmd == "help":
            print_help()
        elif cmd in {"add","sub","mul","div","pow","root"}:
            try:
                a, b = parse_two_numbers(parts)
                result = calc.compute(cmd, a, b)
                print(f"{cmd} {a} {b} = {result}")
            except (ValidationError, OperationError) as e:
                print(f"Error: {e}")
        elif cmd == "history":
            if calc.history.df.empty:
                print("(no history)")
            else:
                # simple print
                print(calc.history.df.to_string(index=False))
        elif cmd == "undo":
            try:
                calc.undo()
                print("OK: undo")
            except UndoRedoError as e:
                print(f"Error: {e}")
        elif cmd == "redo":
            try:
                calc.redo()
                print("OK: redo")
            except UndoRedoError as e:
                print(f"Error: {e}")
        elif cmd == "clear":
            calc.clear()
            print("OK: cleared")
        elif cmd == "save":
            path = parts[1] if len(parts) > 1 else None
            calc.save(path)
            print("OK: saved")
        elif cmd == "load":
            path = parts[1] if len(parts) > 1 else None
            try:
                calc.load(path)
                print("OK: loaded")
            except FileNotFoundError:
                print("Error: file not found")
        else:
            print("Unknown command. Type 'help'.")
    return 0

if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
