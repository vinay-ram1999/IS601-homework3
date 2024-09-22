"""Contains the Recors class which stores all calculations performed by the Calculator class along with its output in a dict"""

from typing import Dict, Tuple
from decimal import Decimal
from calculator.calculation import SingleInpCalculation, DualInpCalculation

class Records:
    history: Dict[object, Decimal] = {}

    @classmethod
    def add_calculation(cls, calculation: object):
        """Add a new calculation record to the history."""
        cls.history[calculation] = calculation.evaluate()

    @classmethod
    def get_history(cls) -> Dict[object, Decimal]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest_record(cls) -> object:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return list(cls.history)[-1]
        return None
    
    @classmethod
    def get_latest_calculation(cls) -> Tuple:
        """Get the latest calculation along with its result value in a tuple. Returns None if there's no history."""
        if cls.history:
            return list(cls.history.items())[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> Dict[object, Decimal]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history.keys() if calc.operation.__name__ == operation_name]

