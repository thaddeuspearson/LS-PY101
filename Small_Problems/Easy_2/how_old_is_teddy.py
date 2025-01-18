"""
Build a program that randomly generates and prints Teddy's age. To get the age
you should generate a random number between 20 and 100, inclusive.
"""
import sys
from random import randint


def teddys_age(name=""):
    """Returns a string that includes Teddy's randomly generatred age

    :name (str): The name of the Teddy bear
    :returns (str): Random age of Teddy string
    """
    if not name:
        name = input("What is the name of your bear? ") or "Teddy"
    return f"{name} is {randint(20, 100)} years old!"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 5, the randint function is imported from the random module. This will
return a random integer between the two arguments passed to it inclusively.
Combining this with string interpolation, the formatted string with Teddy's
randomly generated age is returned when teddys_age is called.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        TEDDY_STR = teddys_age("Teddy")
        AGE = int(TEDDY_STR[9:TEDDY_STR.index(" ", 10)])
        assert isinstance(TEDDY_STR, str), "Should return a string"
        assert TEDDY_STR[:5] == "Teddy", "Name should be Teddy"
        assert (21 <= len(TEDDY_STR) <= 23), "Should between 21 and 23 chars"
        assert 20 <= AGE <= 100, "Age should be between 20 and 100 inclusively"
    else:
        print(teddys_age())
