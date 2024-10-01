'''Test calculation'''

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# Import pytest for writing test cases.
# Import the DualInpCalculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import SingleInpCalculation, DualInpCalculation
from calculator.operations import add, divide, sigma

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.
#@pytest.mark.parametrize("a, b, operation, expected", [
#    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Test addition
#    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Test subtraction
#    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
#    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
#    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Test addition with decimals
#    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Test subtraction with decimals
#    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
#    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
#])

def test_dual_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the DualInpCalculation class correctly evaluates the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to evaluate.
        expected (Decimal): The expected result of the operation.
    """
    calc = DualInpCalculation(a, b, operation) # Create a DualInpCalculation instance with the provided operands and operation.
    assert calc.evaluate() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_single_calculation_operations(a, operation, expected):
    """Test sigma calculations"""
    calc = SingleInpCalculation(a, operation) # Create a SingleInpCalculation instance with the provided operands and operation.
    assert calc.evaluate() == expected, f"Failed {operation.__name__} operation with {a}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the DualInpCalculation class.
    
    This test verifies that the __repr__ method of a DualInpCalculation instance returns a string
    that accurately represents the state of the DualInpCalculation object, including its operands and operation.
    """
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), add)  # Create a DualInpCalculation instance for testing.
    expected_repr = "DualInpCalculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.
    calc = SingleInpCalculation(int(5), sigma)  # Create a SingleInpCalculation instance for testing.
    expected_repr = "SingleInpCalculation(5, sigma)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to evaluate a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = DualInpCalculation(Decimal('10'), Decimal('0'), divide)  # Create a DualInpCalculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.evaluate()  # Attempt to evaluate the calculation, which should trigger the ValueError.

def test_sum_of_negative():
    """Test negative number for sigma operation"""
    calc = SingleInpCalculation(int(-5), sigma)
    with pytest.raises(ValueError, match="Please enter an integer > 0"):  # Expect a ValueError to be raised.
        calc.evaluate()  # Attempt to evaluate the calculation, which should trigger the ValueError.
