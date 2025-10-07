# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025


import pandas as pd
from typing import List, Protocol
from .exceptions import UndoRedoError
import warnings

# Suppress pandas warnings for clean output
warnings.filterwarnings("ignore", category=FutureWarning)

#  Observer Pattern 
class HistoryObserver(Protocol):
    def on_history_changed(self, df: pd.DataFrame) -> None:
        ...


class HistorySubject:
    def __init__(self):
        self._observers: List[HistoryObserver] = []

    def attach(self, obs: HistoryObserver):  # pragma: no cover
        if obs not in self._observers:
            self._observers.append(obs)

    def detach(self, obs: HistoryObserver):  # pragma: no cover
        if obs in self._observers:
            self._observers.remove(obs)

    def notify(self, df: pd.DataFrame):
        for obs in list(self._observers):
            obs.on_history_changed(df)


class AutoSaveObserver:
    def __init__(self, path_getter):
        self._path_getter = path_getter

    def on_history_changed(self, df: pd.DataFrame):
        path = self._path_getter()
        df.to_csv(path, index=False)


# History with pandas
class History(HistorySubject):
    COLS = ["op", "a", "b", "result", "error"]

    def __init__(self):
        super().__init__()
        self.df = pd.DataFrame(columns=self.COLS)

    def add(self, op: str, a: float, b: float, result: float | None, error: str | None):
        """Add a new calculation record to the DataFrame and notify observers."""
        row = {"op": op, "a": a, "b": b, "result": result, "error": error}

        # handle empty DataFrame safely 
        if self.df.empty:
            self.df = pd.DataFrame([row])
        else:
            self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)

        self.notify(self.df)

    def clear(self):
        """Clear all history records."""
        self.df = pd.DataFrame(columns=self.COLS)
        self.notify(self.df)

    def load_csv(self, path: str):
        """Load history from a CSV file, ensuring required columns exist."""
        self.df = pd.read_csv(path) if path else self.df

        # Ensure all required columns exist
        for c in self.COLS:
            if c not in self.df.columns:
                self.df[c] = None
        self.df = self.df[self.COLS]
        self.notify(self.df)

    def save_csv(self, path: str):
        """Save current history to a CSV file."""
        self.df.to_csv(path, index=False)


# Memento Pattern
class HistoryMemento:
    def __init__(self, df: pd.DataFrame):
        self.state = df.copy(deep=True)


class Caretaker:
    def __init__(self, history: History):
        self.history = history
        self._undo: List[HistoryMemento] = []
        self._redo: List[HistoryMemento] = []

    def snapshot(self):
        """Save current state for potential undo."""
        self._undo.append(HistoryMemento(self.history.df))
        self._redo.clear()

    def undo(self):
        """Revert to previous state."""
        if not self._undo:
            raise UndoRedoError("Nothing to undo")
        m = self._undo.pop()
        self._redo.append(HistoryMemento(self.history.df))
        self.history.df = m.state
        self.history.notify(self.history.df)

    def redo(self):
        """Reapply the last undone change."""
        if not self._redo:
            raise UndoRedoError("Nothing to redo")
        m = self._redo.pop()
        self._undo.append(HistoryMemento(self.history.df))
        self.history.df = m.state
        self.history.notify(self.history.df)
