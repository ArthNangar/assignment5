# Name : ARTH RANCHHODBHAI NANGAR
# DATE : 10/6/2025

from dataclasses import dataclass
from .operations import operation_factory
from .exceptions import OperationError

@dataclass
class Calculation:
    op: str
    a: float
    b: float

    def execute(self) -> float:
        strategy = operation_factory(self.op)
        return strategy.execute(self.a, self.b)
