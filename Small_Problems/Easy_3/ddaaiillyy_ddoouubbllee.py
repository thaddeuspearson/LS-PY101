"""
Write a function that takes a string argument and returns a new string that
contains the value of the original string with all consecutive duplicate
characters collapsed into a single character.
"""


def crunch(string):
    """returns the given string value with all duplicate characters removed.

    :string (str): The string to crunch duplicates from
    :returns return str (str): the crunched string.
    """
    return_str = ""

    for char in string:
        if return_str == "" or char != return_str[-1]:
            return_str += char
    return return_str


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 8, the cruch function is defined with 1 parameter, string.
On line 14, the local variable return_str is initialized with an empty string.
The for loop on line 16 iterates through the string one char at a time. With
each iteration, the if conditional statement on line 17 checkes to see if
return_str is empty, or if the last character in it is the same as the current
character in the current iteration. If either of those conditions have a truthy
value, the current char is concatenated to return_str, and it is returned on
line 19 after the loop has finished executing.
"""


# Test Cases
if __name__ == "__main__":
    assert crunch('ddaaiillyy ddoouubbllee') == 'daily double'
    assert crunch('4444abcabccba') == '4abcabcba'
    assert crunch('ggggggggggggggg') == 'g'
    assert crunch('abc') == 'abc'
    assert crunch('a') == 'a'
    assert crunch('') == ''
