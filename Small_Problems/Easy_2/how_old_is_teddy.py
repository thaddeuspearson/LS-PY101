"""
Build a program that randomly generates and prints Teddy's age. To get the age
you should generate a random number between 20 and 100, inclusive.
"""
from random import randint


def teddys_age():
    """Returns a string that includes Teddy's randomly generatred age

    :returns (str): Random age of Teddy string
    """
    return f"Teddy is {randint(20, 100)} years old!"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 5, the randint function is imported from the random module. This will
return a random integer between the two arguments passed to it inclusively.
Combining this with string interpolation, the formatted string with Teddy's
randomly generated age is returned when teddys_age is called.
"""


# Test Cases
if __name__ == "__main__":
    AGE_STR = teddys_age()
    AGE = int(AGE_STR[9:AGE_STR.index(" ", 10)])
    assert isinstance(AGE_STR, str), "Should return a string"
    assert (21 <= len(AGE_STR) <= 23), "Should between 21 and 23 chars"
    assert 20 <= AGE <= 100, "Should be between 20 and 100 inclusively"
