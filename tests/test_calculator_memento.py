# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025


from app.calculator_memento import HistoryMemento, Caretaker
from app.history import History

def test_reexport():
    h = History()
    c = Caretaker(h)
    assert hasattr(c, "snapshot")
