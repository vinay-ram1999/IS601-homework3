"""Contains the main Calculator class"""

from calculator.records import Records  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide, sigma  # Arithmetic operations
from calculator.calculation import DualInpCalculation, SingleInpCalculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_dualinp_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = DualInpCalculation.create(a, b, operation)
        Records.add_calculation(calculation)
        return calculation.evaluate()
    
    @staticmethod
    def _perform_singleinp_operation(a: Decimal, operation: Callable):
        calculation = SingleInpCalculation.create(a, operation)
        Records.add_calculation(calculation)
        return calculation.evaluate()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_dualinp_operation method with the add operation
        return Calculator._perform_dualinp_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_dualinp_operation method with the subtract operation
        return Calculator._perform_dualinp_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_dualinp_operation method with the multiply operation
        return Calculator._perform_dualinp_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_dualinp_operation method with the divide operation
        return Calculator._perform_dualinp_operation(a, b, divide)
    
    @staticmethod
    def sigma(a: int) -> int:
        return Calculator._perform_singleinp_operation(a, sigma)
