"""
Write an xor function that takes two arguments, and returns True if exactly
one of its arguments is truthy, False otherwise.
"""


def xor(left_expression, right_expression):
    """Returns an exclusive or (XOR) operation on the two given expressions.
    
    :left_expression (many): the expression on the left side of the xor
    :right_expression (many): the expression on the right side of the xor
    :returns (bool): True/False if the operation is a valid XOR
    """
    return bool(left_expression) + bool(right_expression) == 1


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 7, the xor function is defined with two parameters, left_expression
and right_expression. When called with two vaild expressions], this function
coerces both arguments to their boolean representation, and adds them
together. Since booleans evaluate to 1 if True, 0 if false, in the result of
the addition operation is exactly 1,  then the XOR statement is valid, and
True is returned. False is returned in the opposite case.
"""


# Test Cases
if __name__ == "__main__":
    assert xor(5, 0)
    assert xor(False, True)
    assert not xor(1, 1)
    assert not xor(True, True)
