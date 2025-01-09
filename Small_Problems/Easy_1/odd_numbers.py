"""
Print all odd numbers from 1 to 99, inclusive, with each
number on a separate line. Can you solve the problem by
iterating over just the odd numbers?
"""


def print_odds(start, end):
    """Prints odd numbers inclusively contained within the given range.

    :start (int): the number beginning the range
    :end (int): the number ending the range
    :returns (NoneType): None
    """
    start = start + 1 if start % 2 == 0 else start
    end = end - 1 if end % 2 == 0 else end

    for odd_num in range(start, end + 1, 2):
        print(odd_num)


# Test Cases
assert print_odds(1, 99) is None, "print_odds returns None."
