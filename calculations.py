# calculations.py

import math


def calculate_D8D(log_ne, epsilon, x, y, c):
    """
    Calculate the 8D Fractal Dimension using the provided parameters.

    Parameters:
    log_ne (float): Logarithmic value of 'ne'
    epsilon (float): A small positive number
    x (float): Exponent associated with log_ne
    y (float): Exponent associated with epsilon
    c (float): Constant

    Returns:
    float: Computed 8D Fractal Dimension

    Raises:
    ValueError: If epsilon or any of the input values are invalid.
    """
    if epsilon <= 0:
        raise ValueError("Epsilon must be a small positive number")

    if any(map(lambda v: not isinstance(v, (int, float)), [log_ne, epsilon, x, y, c])):
        raise ValueError("All inputs must be numeric values")

    try:
        result = (log_ne ** x) / (epsilon ** (x + y) * (math.log(1 / epsilon) + c) ** y)
        return result
    except ZeroDivisionError:
        return float('inf')


if __name__ == "__main__":
    import argparse


    def parse_arguments():
        parser = argparse.ArgumentParser(description="Calculate the 8D Fractal Dimension")
        parser.add_argument("log_ne", type=float, help="Logarithmic value of 'ne'")
        parser.add_argument("epsilon", type=float, help="A small positive number")
        parser.add_argument("x", type=float, help="Exponent associated with log_ne")
        parser.add_argument("y", type=float, help="Exponent associated with epsilon")
        parser.add_argument("c", type=float, help="Constant")

        return parser.parse_args()


    args = parse_arguments()

    try:
        result = calculate_D8D(args.log_ne, args.epsilon, args.x, args.y, args.c)
        print(f"Calculated 8D Fractal Dimension: {result}")
    except ValueError as e:
        print(f"Error: {e}")
