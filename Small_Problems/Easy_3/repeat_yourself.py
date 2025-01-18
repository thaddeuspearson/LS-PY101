"""
Write a function that takes two arguments, a string and a positive integer,
then prints the string as many times as the integer indicates.
"""


def repeat(string, times_to_repeat):
    """Returns the given string value repeated the number of times indicated.

    :string (str): given string to repeat
    :times_to_repeat (int): The number of times to reapeat the string
    """
    return (f"{string}\n" * times_to_repeat)


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 7, the repeat function is defined with two parameters, string and
times_to_repeat. On line 13, using interpolation and string multiplication,
the formatted string (with necessary newlines) is returned
"""


# Test Cases
if __name__ == "__main__":
    assert repeat('Hello', 3) == "Hello\nHello\nHello\n"
    assert repeat('', 5) == "\n\n\n\n\n"
    assert repeat(' ', 4) == " \n \n \n \n"
