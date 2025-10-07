# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

import os
import pandas as pd
from app.history import History, AutoSaveObserver, Caretaker
from app.exceptions import UndoRedoError

def test_history_add_and_clear(tmp_path):
    h = History()
    h.add("add",1,2,3,None)
    assert len(h.df) == 1
    h.clear()
    assert len(h.df) == 0

def test_autosave_observer(tmp_path):
    path = tmp_path/"h.csv"
    h = History()
    h.attach(AutoSaveObserver(lambda: str(path)))
    h.add("add",1,2,3,None)
    assert path.exists()
    df = pd.read_csv(path)
    assert len(df) == 1

def test_load_save(tmp_path):
    path = tmp_path/"h.csv"
    h = History()
    h.add("add",1,2,3,None)
    h.save_csv(str(path))

    h2 = History()
    h2.load_csv(str(path))
    assert len(h2.df) == 1

def test_memento_undo_redo():
    h = History()
    c = Caretaker(h)
    c.snapshot()
    h.add("add",1,2,3,None)
    c.undo()
    assert len(h.df) == 0
    c.redo()
    assert len(h.df) == 1

def test_memento_errors():
    h = History()
    c = Caretaker(h)
    try:
        c.undo()
        assert False, "expected error"
    except UndoRedoError:
        pass
    try:
        c.redo()
        assert False, "expected error"
    except UndoRedoError:
        pass
