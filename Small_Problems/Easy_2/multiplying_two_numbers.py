"""
Create a function that takes two arguments, multiplies them together,
and returns the result.
"""


def multiply(num_1, num_2):
    """Multiplies two operands together.

    :num_1 (int): the first operand
    :num_2 (int): the second operand
    :returns (int): num_1 * num_2
    """
    return num_1 * num_2


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 7, the multiply finction is defined with two parameters,
num_1 and num_2. When executed with two number types passed to
num_1 and num_2 as arguments, the multiply function returns the
value of num_1 * num_2.
"""


# Test Cases
if __name__ == "__main__":
    assert multiply(5, 3) == 15
    assert multiply(1, 0) == 0
    assert multiply(-1, 10) == -10
