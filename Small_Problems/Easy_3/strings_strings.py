"""
Write a function that takes one argument, a positive integer, and returns a
string of alternating '1's and '0's, always starting with a '1'. The length of
the string should match the given integer.
"""


def stringy(num):
    """Returns an alternating sequence of 1s and 0s based on the num value.

    :num (int): the num to populate 1s and 0s to
    :returns return_str (str): the string of 1s and 0s
    """
    return_str = ""

    for n in range(num):
        return_str += '1' if n % 2 == 0 else '0'
    return return_str


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 8, the stringy function is defined with a single parameter, num.
Upon execution with a valid integer value passed to num as an argument,
a local variable named return_str is created and assigned to an empty
string on line 14.

On line 16, a for loop iterates theough a range object that is initialized
to the value of num, ensuring that the loop runs n times. In each iteration,
the return_str has a 1 or a 0 concatenated to it determined by the if/else
conditional block testing if n is even or odd using the modulo 2/strict
equality technique. After the loop is finished, return_str is returned on
line 18.
"""


# Test Cases
if __name__ == "__main__":
    assert stringy(6) == "101010", "Should be True"
    assert stringy(9) == "101010101", "Should be True"
    assert stringy(4) == "1010", "Should be True"
    assert stringy(7) == "1010101", "Should be True"
