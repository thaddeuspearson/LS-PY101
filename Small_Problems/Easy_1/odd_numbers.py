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

    for odd_num in range(start, end + 1, 2):
        print(odd_num)


# Test Cases
if __name__ == "__main__":
    assert print_odds(1, 102) is None, "print_odds returns None."
