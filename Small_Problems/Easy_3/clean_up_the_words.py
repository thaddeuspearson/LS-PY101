"""
Given a string that consists of some words and an assortment of non-alphabetic
characters, write a function that returns that string with all of the
non-alphabetic characters replaced by spaces. If one or more non-alphabetic
characters occur in a row, you should only have one space in the result 
(i.e., the result string should never have consecutive spaces).
"""


def clean_up(string):
    """Replaces all non-alphabetic characters and replaces with a space.

    :string (str): The string to clean up
    :returns clean_str (str): The "cleaned up" string
    """
    clean_str = ""
    for c in string:
        if c.isalpha():
            clean_str += c
        elif not clean_str or clean_str[-1] != " ":
            clean_str += " "
    return clean_str


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 10, the clean_up function is defined with a single parameter, string.
On line 16, a local variable named clean_str is set to the value of an empty
string. This will accumulate as the for loop on line 17 moves through each
character of string.

On line 18, c is checked if it is an alphabetic character with .isalpha().
If it is, it is added to clean_str. If it is not, and clean_string is either
empty, or the last character in clean_str is not a space, then a space is
concatenated to clean_str.
"""


# Test Cases
if __name__ == "__main__":
    assert clean_up("---what's my +*& line?") == " what s my line "
