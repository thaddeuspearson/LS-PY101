"""
Write a function that returns a list that contains every other element of a
list that is passed in as an argument. The values in the returned list should
be those values that are in the 1st, 3rd, 5th, and so on elements of the
argument list.
"""


def oddities(input_list):
    """Returns every other element in the given input list starting with the
    first element.

    :input_list (list): the list to filter
    :returns (list): every other element in input_list
    """
    return [l for i, l in enumerate(input_list) if i % 2 == 0]


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 9, the oddities function is defined with one parameter, input_list.
This function returns a list comprehension.

The list comprehension on line 16 loops through the an enumeration iterable
conctrusted from input_list. THis gives access to both the index of each
element (denoted with i), and the element itself (denoted with l). At each
iteration, the if statement at the end is checked to ensure the index is even
using the modulo/strict equality operator to test for parity. If the statement
is truthy, the list at that index is appended to the return list.

At the end of the loop, the filtered list is returned, and execution completes.
"""


# Test Cases
if __name__ == "__main__":
    assert oddities([2, 3, 4, 5, 6]) == [2, 4, 6], "Should be True"
    assert oddities([1, 2, 3, 4]) == [1, 3], "Should be True"
    assert oddities(["abc", "def"]) == ['abc'], "Should be True"
    assert oddities([123]) == [123], "Should be True"
    assert oddities([]) == [], "Should be True"
