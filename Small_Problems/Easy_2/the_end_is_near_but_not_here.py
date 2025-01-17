"""
Write a function that returns the next to last word in the string argument.
Words are any sequence of non-blank characters. You may assume that the input
string will always contain at least two words.
"""


def penultimate(input_str):
    """Returns the second to last word in the given string.

    :input_str (str): the string to process
    :returns (str): the second to last word in input_str
    """
    return input_str.split()[-2]


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 8, the penultimate function is defined with one parameter, input_str.

When called with a string argument passed to input_str, penultimate splits out
input_str to a list, and then using bracket notation, gets the second to last
word in the list using a negative index. This value is returned and execution
completes.
"""


# Test Cases
if __name__ == "__main__":
    assert penultimate("last word") == "last"
    assert penultimate("Launch School is great!") == "is"
