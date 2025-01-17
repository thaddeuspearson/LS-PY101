"""
Write a function that computes the sum of all numbers between 1 and
some other number, inclusive, that are multiples of 3 or 5. For
instance, if the supplied number is 20, the result should be 98
(3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.
"""


def multisum(end_num):
    """Sums up all the integer values between 1 and the end_num if
    the integer value is a multiple of 3 or 5.

    :end_num (int): the number to sum up to
    """
    return sum([n for n in range(1, end_num+1) if (n % 3 == 0 or n % 5 == 0)])


"""CODE EXPLAINATION
On line 11, the function multisum is defined with a single parameter called
end_num, which expects an integer value when multisum is called. This function
uses a list comprehension passed to the sum built-in function. Sum accepts a
list as an argument and returns the sum of all the elements of the list that
was passed to it.

Within the list comprehension, the for loop mechanism uses the range funtion to
create an iterable, beginning at 1 and continuing until the iterator n is equal
to the value of end_num+1, since the second parameter for the range function is
excluded by default. With each iteration, n is compared to 3 or 5 with the
modulo/strict equality technique of determining if either number is a factor
of n. If either condition returns True, the or statement evaluates to True and
n is appended to the resulting list. If either condition is not True, then the
iteration continues.

The return keyword returns the sum of the list that was generated.
"""


# Test Cases
if __name__ == "__main__":
    assert multisum(3) == 3
    assert multisum(5) == 8
    assert multisum(10) == 33
    assert multisum(1000) == 234168
