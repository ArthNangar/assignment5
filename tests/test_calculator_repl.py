# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import builtins
import os
import pytest
from app.calculator_repl import CalculatorFacade, main

def test_facade_compute_and_history(tmp_path, monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", str(tmp_path/"h.csv"))
    monkeypatch.setenv("AUTOSAVE", "false")
    calc = CalculatorFacade()
    r = calc.compute("add", 1, 2)
    assert r == 3
    assert len(calc.history.df) == 1
    calc.undo()
    assert len(calc.history.df) == 0
    calc.redo()
    assert len(calc.history.df) == 1
    calc.clear()
    assert calc.history.df.empty

def test_repl_all_paths(monkeypatch, tmp_path):
    # Cover all REPL command branches
    hist_path = str(tmp_path / "hist.csv")
    monkeypatch.setenv("HISTORY_FILE", hist_path)
    monkeypatch.setenv("AUTOSAVE", "false")

    inputs = iter([
        "help\n",
        "add 1 2\n",
        "sub 5 3\n",
        "mul 2 3\n",
        "div 4 2\n",
        "pow 2 3\n",
        "root 9 2\n",
        "div 4 0\n",        # division error
        "unknowncmd\n",     # invalid command
        "history\n",
        "undo\n",
        "redo\n",
        "clear\n",
        f"save {hist_path}\n",
        f"load {hist_path}\n",
        "exit\n",
    ])

    def fake_input(prompt=""):
        try:
            return next(inputs).strip()
        except StopIteration:
            raise EOFError

    monkeypatch.setattr(builtins, "input", fake_input)
    assert main() == 0
    assert os.path.exists(hist_path)

# Added after changes 
def test_repl_edge_paths(monkeypatch):
    # Covers unknown and empty input + quit aliases
    inputs = iter([
        "\n",            # empty
        "quit\n",        # alias for exit
    ])
    def fake_input(prompt=""):
        try:
            return next(inputs).strip()
        except StopIteration:
            raise EOFError
    monkeypatch.setattr("builtins.input", fake_input)
    from app.calculator_repl import main
    assert main() == 0

def test_repl_final_branches(monkeypatch):
    """Covers unknown command and EOF exit branches."""
    inputs = iter([
        "foobar\n",  # unknown command
    ])

    def fake_input(prompt=""):
        try:
            return next(inputs).strip()
        except StopIteration:
            raise EOFError

    monkeypatch.setattr("builtins.input", fake_input)
    from app.calculator_repl import main
    assert main() == 0


def test_repl_empty_and_quit(monkeypatch):
    """Covers empty input and 'quit' alias."""
    inputs = iter([
        "\n",       # empty input
        "quit\n",   # quit alias
    ])

    def fake_input(prompt=""):
        try:
            return next(inputs).strip()
        except StopIteration:
            raise EOFError

    monkeypatch.setattr("builtins.input", fake_input)
    from app.calculator_repl import main
    assert main() == 0

