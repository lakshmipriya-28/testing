from src.utils.math_utils import add, subtract, multiply, divide

class Calculator:
    """Performs basic arithmetic operations using utility functions."""

    def __init__(self):
        self.history = []

    def compute(self, a: float, b: float, op: str) -> float:
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        else:
            raise ValueError(f"Unsupported operation: {op}")

        self.history.append((a, op, b, result))
        return result

    def get_history(self):
        return self.history
