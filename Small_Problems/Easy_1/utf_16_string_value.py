"""
Write a function that determines and returns the UTF-16 string value
of a string passed in as an argument. The UTF-16 string value is the
sum of the UTF-16 values of every character in the string. (You may
use ord to determine the UTF-16 value of a character.)
"""


def utf16_value(string):
    """Returns the sum of all the UTF-16 values of the chars in string

    :param string (str): the string to sum
    :returns (int): the sum of all the UTF-16 char values in string
    """
    return sum([ord(char) for char in string])


"""CODE EXPLAINATION
On line 9, the function utf16_value is defined with a single parameter
named string. When this function is called with a string argument, the
sum built-in function is called on a list comprehension. The list
comprehension loops through each character in string, and uses the ord
built-in function to return the UTF-16 value for the character, and
append this value to the resulting list. When the loop has finished, the
final list is passed to the sum function, and resulting sum is returned.
"""


# Test Cases
if __name__ == "__main__":
    assert utf16_value('Four score') == 984
    assert utf16_value('Launch School') == 1251
    assert utf16_value('a') == 97
    assert utf16_value('') == 0
    OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
    assert utf16_value(OMEGA) == 937
    assert utf16_value(OMEGA + OMEGA + OMEGA) == 2811
