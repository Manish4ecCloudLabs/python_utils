"""Basic calculator with add, subtract, multiply, divide and power functions."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a + b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The result of a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a * b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing one number by another.

    Args:
        a: The number to be divided (dividend).
        b: The number to divide by (divisor).

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return a number raised to the power of another.

    Args:
        base: The number to be raised.
        exponent: The power to raise the base to.

    Returns:
        The result of base ** exponent.

    Raises:
        ValueError: If base is zero and exponent is negative.
    """
    if base == 0 and exponent < 0:
        raise ValueError("cannot raise zero to a negative power")
    return base ** exponent


if __name__ == "__main__":
    print("Basic Calculator")
    print("----------------")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")
    print(f"2 ** 3  = {power(2, 3)}")
    try:
        print(f"10 / 0  = {divide(10, 0)}")
    except ValueError as error:
        print(f"10 / 0  = Error: {error}")
