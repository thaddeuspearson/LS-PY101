"""
Print all even numbers from 1 to 99, inclusive, with each
number on a separate line. Can you solve the problem by
iterating over just the even numbers?
"""


def print_evens(start, end):
    """Prints even numbers inclusively contained within the given range.

    :start (int): the number beginning the range
    :end (int): the number ending the range
    :returns (NoneType): None
    """
    start = start + 1 if start % 2 == 1 else start

    for even_num in range(start, end + 1, 2):
        print(even_num)


# Test Cases
if __name__ == "__main__":
    assert print_evens(1, 102) is None, "print_evens returns None."
