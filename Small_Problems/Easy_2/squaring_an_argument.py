"""
Using the multiply function from the "Multiplying Two Numbers" exercise,
write a function that computes the square of its argument (the square is
the result of multiplying a number by itself).
"""
from multiplying_two_numbers import multiply


def square(num):
    """Squares the given number.

    :num (int): the nuber to square
    :returns (int): num squared
    """
    return multiply(num, num)


"""CODE EXPLAINATION
On line 6, the multiply function is imported from the 
multiplying_two_numbers.py exercise script.

On line 9, the square function is defined with one parameter, num.
When called with an integer value as an argument for num, the square
funtion makes a call to the multiply function, and provides the num
argument as two separate arguments to the multiply function.

The multiply function takes those arguments, and returns them multiplied
together (squaring the given number) back to the square function. Finally,
the square function returns that returned value and execution completes.
"""


# Test Cases
if __name__ == "__main__":
    assert square(5) == 25
    assert square(-8) == 64
    assert square(0) == 0
