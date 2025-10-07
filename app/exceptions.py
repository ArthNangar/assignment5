# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

class CalculatorError(Exception):
    """Base exception for calculator."""

class ConfigurationError(CalculatorError):
    """Raised for invalid configuration."""

class ValidationError(CalculatorError):
    """Raised for invalid user input."""

class OperationError(CalculatorError):
    """Raised for operation execution errors."""

class UndoRedoError(CalculatorError):
    """Raised when undo/redo is not possible."""
