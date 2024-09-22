'''Test Operations'''

from decimal import Decimal
import pytest
from calculator.calculation import SingleInpCalculation, DualInpCalculation
from calculator.operations import add, subtract, multiply, divide, sigma


def test_operation_add():
    '''Testing the addition operation'''
    calculation = DualInpCalculation(Decimal('10'), Decimal('5'), add)
    assert calculation.evaluate() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = DualInpCalculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.evaluate() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = DualInpCalculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.evaluate() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = DualInpCalculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.evaluate() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = DualInpCalculation(Decimal('10'), Decimal('0'), divide)
        calculation.evaluate()

def test_operation_sigma():
    '''Test the sigma operation'''
    n = 100
    calculation = SingleInpCalculation(n, sigma)
    assert calculation.evaluate() == 5050, "Sigma operation failed"
