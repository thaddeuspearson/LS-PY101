"""
A double number is an even-length number whose left-side digits are exactly
the same as its right-side digits. For example, 44, 3333, 103103, and 7676
are all double numbers, whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied
by two, unless the argument is a double number. If the argument is a double
number, return the double number as-is.
"""


def twice(num):
    """Returns a double number, or a number doubled depending on if the given
    number is a double number or not.

    :num (int): the number to return or double
    :returns (int) num or 2 * n
    """
    first_half = str(num)[:(len(str(num)) // 2)]
    second_half = str(num)[(len(str(num)) // 2):]
    return num if first_half == second_half else num * 2


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 12 the twice function is defined with a single parameter num. On lines
19 and 20, 2 local variables (first_half and second_half) are defined and set
to string slices of the argument passed to the num parameter during execution.

On line 21, the return statement uses a ternary expression to check if
first_half is equal to second_half. If it is, then the original number is
returned. If not, then the original number is doubled.
"""


# Test Cases
if __name__ == "__main__":
    assert twice(37) == 74, "Should be True"
    assert twice(44) == 44, "Should be True"
    assert twice(334433) == 668866, "Should be True"
    assert twice(444) == 888, "Should be True"
    assert twice(107) == 214, "Should be True"
    assert twice(103103) == 103103, "Should be True"
    assert twice(3333) == 3333, "Should be True"
    assert twice(7676) == 7676, "Should be True"
