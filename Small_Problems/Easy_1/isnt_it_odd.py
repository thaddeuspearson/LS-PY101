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


# Test Cases
if __name__ == "__main__":
    assert is_odd(5), "5 is odd."
    assert not is_odd(6), "6 is even."
    assert is_odd(-1), "The absolute value of -1 is odd."
    assert not is_odd(-2), "The absolute value of -2 is even."
    assert not is_odd(0), "The absolute value of 0 is even."
