"""
Print all odd numbers from 1 to 99, inclusive, with each 
number on a separate line. Can you solve the problem by 
iterating over just the odd numbers?
"""


def print_odds(start=1, end=99):
    """Prints odd numbers inclusively contained within the given range.

    :start (int): the number beginning the range (default 1)
    :end (int): the number ending the range (default 99)
    :returns (NoneType): None
    """
    start = start + 1 if start % 2 == 0 else start

    for odd_num in range(start, end + 1, 2):
        print(odd_num)


# Test Cases
assert print_odds() is None, "print_odds returns None."
