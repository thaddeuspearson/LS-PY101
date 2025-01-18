"""
Write a function that takes a number as an argument. If the argument
is a positive number, return the negative of that number. If the
argument is a negative number, return it as-is.
"""


def negative(integer):
    """Returns a negative reporesentation of the given integer.
    
    :integer (int): the integer to make negative
    :return (int): the integer coerced to be negative
    """
    return -integer if integer > 0 else integer

# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 8, the negative function is defined, with a single parameter, integer.
On line 14, the if conditional statement checks to see if argument passed to
integer when calling negative is greater than or equal to 0. If it is, it
returns the integer coerced to a negative value. Otherwise, it returns the
integer value aas-is, since it is already negative.
"""


# Test Cases
if __name__ == "__main__":
    assert negative(5) == -5, "Should be True"
    assert negative(-3) == -3, "Should be True"
    assert negative(0) == 0, "Should be True"
