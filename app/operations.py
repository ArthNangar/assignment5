# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025


from abc import ABC, abstractmethod
from .exceptions import OperationError

# Strategy Pattern: each operation is a strategy
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...

class Add(OperationStrategy):
    def execute(self, a, b): return a + b

class Sub(OperationStrategy):
    def execute(self, a, b): return a - b

class Mul(OperationStrategy):
    def execute(self, a, b): return a * b

class Div(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("division by zero is not allowed.")
        return a / b

class Pow(OperationStrategy):
    def execute(self, a, b): return a ** b

class Root(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("root degree cannot be zero.")
        if a < 0:
            # handle odd/even separately
            if int(b) % 2 == 0:
                raise OperationError("cannot take even root of a negative number.")
            else:
                # compute real odd root of negative base
                return -((-a) ** (1.0 / b))
        try:
            return a ** (1.0 / b)
        except Exception as e:
            raise OperationError(str(e))


# Factory Pattern
def operation_factory(op: str) -> OperationStrategy:
    mapping = {
        "add": Add(),
        "sub": Sub(),
        "mul": Mul(),
        "div": Div(),
        "pow": Pow(),
        "root": Root(),
    }
    try:
        return mapping[op]
    except KeyError as e:
        raise OperationError(f"unknown operation: {op}") from e
