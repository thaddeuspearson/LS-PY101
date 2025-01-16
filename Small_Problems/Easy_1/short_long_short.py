"""SHORT LONG SHORT
Write a function that takes two strings as arguments, determines the
length of the two strings, and then returns the result of concatenating 
the shorter string, the longer string, and the shorter string once again.
You may assume that the strings are of different lengths.
"""


def short_long_short(str_1, str_2):
    (max_s, min_s) = (str_1, str_2) if len(str_1) >= len(str_2) \
                                    else (str_2, str_1)
    return min_s + max_s + min_s


"""CODE EXPLAINATION
On line 8, a function called short_long_short is defined. This function has 2
parameters, str_1, and str_2. On line 10, a ternary statement sets the values
of local variables, max_s and min_s, respectively.

The logic of the ternary statement compares the lengths of str_1 and str_2
with the len() built-in function called on both str_1 and str_2, and and 
compares them with the < operator. Once the longer string is determined, it is
assigned to max_s, and the shorter string is assigned to min_s.

Finally, the return statement on line 11 returns the concatenation of min_s to
max_s to min_s, creating one long string.
"""


# Test Cases
if __name__ == "__main__":
    assert short_long_short("hi", "hey") == "hiheyhi"
    assert short_long_short("yoo", "who") == "whoyoowho"
    assert short_long_short("hello", "hola") == "holahellohola"
    assert short_long_short("", "solo") == "solo"
    assert short_long_short("", "") == ""
