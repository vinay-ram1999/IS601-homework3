"""confest.py"""

#import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, sigma

fake = Faker()

def generate_dual_test_data(num_records):
    """Dual input genrate"""
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_name == 'divide':
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_name == 'divide' and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

def generate_single_test_data(num_records):
    """Single input genrate"""
    operation_mappings = {
        'sigma': sigma
    }
    # Generate test data
    for _ in range(num_records):
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        a = int(fake.random_number(digits=2)) if _ % 4 != 3 else int(fake.random_number(digits=1))
        # Ensure a is not negative
        if operation_name == 'sigma':
            a = abs(a) if a < 0 else a
        try:
            if operation_name == 'sigma' and a < 0:
                expected = "ValueError"
            else:
                expected = operation_func(a)
        except ValueError:
            expected = "ValueError"
        yield a, operation_name, operation_func, expected

def pytest_addoption(parser):
    """adoption"""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """generate tests"""
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "expected"}.intersection(set(metafunc.fixturenames)) and "b" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_dual_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
    elif {"a", "expected"}.intersection(set(metafunc.fixturenames)) and "b" not in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_single_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,operation,expected", modified_parameters)
