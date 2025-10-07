# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

from app.exceptions import CalculatorError, ConfigurationError, ValidationError, OperationError, UndoRedoError

def test_exception_hierarchy():
    assert issubclass(ConfigurationError, CalculatorError)
    assert issubclass(ValidationError, CalculatorError)
    assert issubclass(OperationError, CalculatorError)
    assert issubclass(UndoRedoError, CalculatorError)
