"""
Write a function that takes a positive integer, n, as an argument and prints
a right triangle whose sides each have n stars. The hypotenuse of the triangle
(the diagonal side in the images below) should have one end at the lower-left
of the triangle, and the other end at the upper-right.
"""


def triangle(height):
    """Returns a right triangle string composed of spaces and stars.

    :height (int): the value of the height and the bottom of the right triangle
    :returns triangle_str (str): the formatted triangle string
    """
    return "\n".join([f"{' '*(int(height) - n)}{'*'*n}"
                      for n in range(1, height+1)])


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
The triangle function is defined on line 15, with a single parameter, height.
When called with a valid int argument passed to height, triangle calls the
join function on a newline character with an input list comprehension.

The list comprehension loops from 1 to height + 1, exclusively. At each
iteration f-string interpolation correctly formats the number of spaces and
stars in order to print a right triangle with the bottom level equal to the
value of numstars. Once the loop is finished, and the resulting list
comprehension is passed to the join method, newlines are inserted in between
each formatted string, and the resulting concatenation is returned.
"""


# Test Cases
if __name__ == "__main__":
    assert triangle(5) == "    *\n   **\n  ***\n ****\n*****"
    assert triangle(9) == ("        *\n       **\n      ***\n     ****\n"
                           "    *****\n   ******\n  *******\n ********\n"
                           "*********")
