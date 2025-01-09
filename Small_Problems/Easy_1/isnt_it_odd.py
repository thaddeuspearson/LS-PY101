"""
Write a function that takes one integer argument and returns
True when the number's absolute value is odd, False otherwise.
"""


def is_odd(num):
    """Determines if the absolute value of a given number is odd.

    :num (int): an integer to determine parity
    :returns (bool): True / False if the absolute value num is odd
    """
    return abs(num) % 2 == 1


# Testcases
assert is_odd(5) is True, "5 is odd."
assert is_odd(6) is False, "6 is even."
assert is_odd(-1) is True, "The absolute value of -1 is odd."
assert is_odd(-2) is False, "The absolute value of -2 is even."
assert is_odd(0) is False, "The absolute value of 0 is even."
