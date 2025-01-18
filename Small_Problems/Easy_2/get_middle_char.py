"""
Write a function that takes a non-empty string argument and returns the middle
character(s) of the string. If the string has an odd length, you should return
exactly one character. If the string has an even length, you should return
exactly two characters.
"""


def center_of(string):
    """Retuns the middle character(s) of the given string.
    
    :string (str): The string to return the middle from
    :returns (str): The middle character(s) of string
    """
    mid = len(string) // 2
    return string[mid] if len(string) % 2 != 0 else string[mid-1:mid+1]


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 9 the center_of function is defined with a single parameter, string.
On line 15, a local vafiable mid is declared, and assigned to the value of
dividing the string argument during execution by to and rounding down with
floor division.

The if/else condition block on line 16 tests if the length of the string is
not even with the modulo/strict equality operator. If it is not even, the
middle character is returned, otherwie, the middle two characters are
returned, as the argument passed to string in this case has an even length.
"""


# Test Cases
if __name__ == "__main__":
    assert center_of('I Love Python!!!') == "Py", "Should be True"
    assert center_of('Launch School') == " ", "Should be True"
    assert center_of('Launchschool') == "hs", "Should be True"
    assert center_of('Launch') == "un", "Should be True"
    assert center_of('Launch School is #1') == "h", "Should be True"
    assert center_of('x') == "x", "Should be True"
