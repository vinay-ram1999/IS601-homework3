import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator  # Assuming Calculator is defined as shown previously

class OperationCommand:
    def __init__(self, calculator, operation_name, *args):
        self.calculator = calculator
        self.operation_name = operation_name
        self.args = args

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(*self.args)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_dual_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_single_and_print(a, operation_name):
    try:
        a = int(a)
        command = OperationCommand(Calculator, operation_name, a)
        result = command.execute()
        print(f"The result of {a} {operation_name} is equal to {result}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) == 4:
        _, a, b, operation_name = sys.argv
        calculate_dual_and_print(a, b, operation_name)
    elif len(sys.argv) == 3:
        _, a, operation_name = sys.argv
        calculate_single_and_print(a, operation_name)
    else:
        print("Usage: python calculator_main.py <number1> | <number2> <operation>")
        sys.exit(1)

if __name__ == '__main__':
    main()
