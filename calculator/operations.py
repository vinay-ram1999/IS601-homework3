"""Define the arthematic operations that the calculator can perform with type hints"""

from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sigma(n: int) -> int:
    """Sum of n numbers"""
    if n < 0:
        raise ValueError("Please enter an integer > 0")
    return int(n*(n+1)/2)

