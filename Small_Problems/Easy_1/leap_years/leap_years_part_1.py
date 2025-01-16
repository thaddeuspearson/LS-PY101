"""LEAP YEARS PART ONE
Write a function that takes any year greater than 0 as input and returns
True if the year is a leap year, or False if it is not.

For simplicity, this exercise assumes that the Gregorian calendar has 
been in continuous use since the year 1. We'll address that assumption 
in the next exercise that follows this one.

To determine whether a given year is a leap year, use the rules of the
Gregorian calendar:

    - If the year is divisible by 400, it's a leap year
    - If the year is divisible by 100 but not by 400, it's not a leap year
    - If the year is divisible by 4 but not by 100, it's a leap year
    - All other years are not leap years.
"""


def is_leap_year(year):
    """Calculates if a given year is a leap year. Assumes the rules of the
    Gregorian calendar.

    :year (int): the year to check if it is a leap year
    :returns True/False (Bool)
    """
    return (year % 4 == 0 and year % 100 > 0) or year % 400 == 0


"""CODE EXPLAINATION
On line 19, the function is_leap_year is defined, with a parameter called year.
The Ternary statement handles the control flow for this function.

If statement of the ternary, the modulo operator is used to check if both
4 is a factor and 100 is not a factor of year. When using the modulo operator,
if the remainder of the expression is 0, then the divisor is a factor of the
dividend, and if the remainder is greater than 0, it is not a factor. Since the
logical operator `and` is used between these 2 expressions, both must evaluate
to True in order for the whole statement on the left side of the `or` logical
operator to evaluate to True. The right side of the `or` uses the same tactic,
by checking if 400 is a factor of year.

Any other case is taken care of by the else statement at the end of the ternary
in which case False is returned, since those years are not leap years.
"""


# Test Cases
if __name__ == "__main__":
    assert not is_leap_year(1)
    assert not is_leap_year(2)
    assert not is_leap_year(3)
    assert is_leap_year(4)
    assert not is_leap_year(1000)
    assert not is_leap_year(1100)
    assert is_leap_year(1200)
    assert not is_leap_year(1300)
    assert not is_leap_year(1751)
    assert is_leap_year(1752)
    assert not is_leap_year(1753)
    assert not is_leap_year(1800)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)
    assert not is_leap_year(2023)
    assert is_leap_year(2024)
    assert not is_leap_year(2025)
