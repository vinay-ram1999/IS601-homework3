"""Conatins Calculation class which refers to a single calculation performed by the Calculator"""

from decimal import Decimal
from typing import Callable

class DualInpCalculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return DualInpCalculation(a, b, operation)
    
    def evaluate(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    def __repr__(self) -> str:
        return f"DualInpCalculation({self.a}, {self.b}, {self.operation.__name__})"

class SingleInpCalculation:
    def __init__(self, a: int, operation: Callable):
        self.a = a
        self.operation = operation
    
    @staticmethod
    def create(a: int, operation: Callable):
        return SingleInpCalculation(a, operation)
    
    def evaluate(self) -> int:
        return self.operation(self.a)
    
    def __repr__(self) -> str:
        return f"SingleInpCalculation({self.a}, {self.operation.__name__})"



