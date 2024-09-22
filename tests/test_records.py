'''Test Records'''

# Correct the import order by placing standard library imports before third-party library imports,
# adhering to PEP 8 guidelines for import ordering.
from decimal import Decimal
import pytest

# Import DualInpCalculation and Records classes from the calculator package,
# assuming these are the correct paths following Python's package and module naming conventions.
from calculator.calculation import DualInpCalculation
from calculator.records import Records

# Import arithmetic operation functions (add and subtract) to be tested.
from calculator.operations import add, subtract

# pytest.fixture is a decorator that marks a function as a fixture,
# a setup mechanism used by pytest to initialize a test environment.
# Here, it's used to define a fixture that prepares the test environment for calculations tests.
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    # Clear any existing calculation history to ensure a clean state for each test.
    Records.clear_history()
    # Add sample calculations to the history to set up a known state for testing.
    # These calculations represent typical use cases and allow tests to verify that
    # the history functionality is working as expected.
    Records.add_calculation(DualInpCalculation(Decimal('10'), Decimal('5'), add))
    Records.add_calculation(DualInpCalculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    # Create a new DualInpCalculation object to add to the history.
    calc = DualInpCalculation(Decimal('2'), Decimal('2'), add)
    # Add the calculation to the history.
    Records.add_calculation(calc)
    # Assert that the calculation was added to the history by checking
    # if the latest calculation in the history matches the one we added.
    assert Records.get_latest_record() == calc, "Failed to add the calculation to the history"
    assert Records.get_latest_calculation() == (calc, calc.evaluate()), "Failed to add the calculation and value to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    # Retrieve the calculation history.
    history = Records.get_history()
    # Assert that the history contains exactly 2 calculations,
    # which matches our setup in the setup_calculations fixture.
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    # Clear the calculation history.
    Records.clear_history()
    # Assert that the history is empty by checking its length.
    assert len(Records.get_history()) == 0, "History was not cleared"

def test_get_latest_record(setup_calculations):
    """Test getting the latest calculation from the history."""
    # Retrieve the latest calculation from the history.
    latest = Records.get_latest_record()
    latest_value = Records.get_latest_calculation()
    # Assert that the latest calculation matches the expected values,
    # specifically the operands and operation used in the last added calculation
    # in the setup_calculations fixture.
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"
    assert latest == latest_value[0], "calculation object did not match"
    assert latest_value[0].a == Decimal('20') and latest_value[0].b == Decimal('3'), "Did not get the correct latest calculation"
    assert latest_value[1] == Decimal('17'), "Did not get the correct latest calculation value"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    # Find all calculations with the 'add' operation.
    add_operations = Records.find_by_operation("add")
    # Assert that exactly one calculation with the 'add' operation was found.
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    # Find all calculations with the 'subtract' operation.
    subtract_operations = Records.find_by_operation("subtract")
    # Assert that exactly one calculation with the 'subtract' operation was found.
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_record_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    # Ensure the history is empty by clearing it.
    Records.clear_history()
    # Assert that the latest calculation is None since the history is empty.
    assert Records.get_latest_record() is None, "Expected None for latest calculation with empty history"
    assert Records.get_latest_calculation() is None, "Expected None for latest calculation with empty history"
