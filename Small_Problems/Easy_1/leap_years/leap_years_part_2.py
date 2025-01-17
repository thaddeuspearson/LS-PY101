"""
In the previous exercise, we assumed that the Gregorian calendar 
has been in continuous use since the year 1. However, the 
Gregorian calendar wasn't adopted until much later; prior to that,
much of the world used the Julian calendar, which observed leap 
year every 4 years.

In 1752, England, Ireland, and the British colonies all switched to
the Gregorian calendar. Update the function from the previous
exercise so it uses the Julian calendar prior to 1752, and the
Gregorian calendar starting in 1752.
"""


def is_leap_year(year):
    """Calculates if a given year is a leap year. Assumes the rules of the
    Julian Calendar for years 1-1752, and the Gregorian calendar for years
    after.

    :year (int): the year to check if it is a leap year
    :returns True/False (Bool)
    """
    return (year % 4 == 0 and year % 100 > 0) or year % 400 == 0 \
        if year >= 1752 else year % 4 == 0


"""CODE EXPLAINATION
On line 15, the function is_leap_year is defined with one parameter named year.
The control flow necessry for this program is capable of being expressed as a
ternary statement, which takes advantage of python's short-circuiting features.

Within the if/else conditional statement at the end of the ternary, year is
compared to 1752 (the year the Julian calendar was exchanged for the Gregorian
calendar). The if statement explicitly checks whether year is greater than or
equal to 1752 and returns True / False accordingly. The else statement checks
if year is evenly divisable by 4 using the modulo operator combined with the
strict equality operator. If the resulting calculation is 0, then 4 is a
factor, and True is returned. False is returned in the opposite case.

The first part of the ternary after the retern keyword uses the same modulo
combined with strict equality technique to check if 4 is a factor of year and
100 is not a factor of year. Since the boolean operator `and` is tying these
expressions together, both must be True to return True. Otherwise False is
returned.

The return keyword returns the resulting boolean True / False according to the
`or` boolean operator. Only one side of the `or` statement is needed to evalate
to True for it be returned. Otherwise False is returned.
"""


# Test Cases
if __name__ == "__main__":
    assert not is_leap_year(1)
    assert not is_leap_year(2)
    assert not is_leap_year(3)
    assert is_leap_year(4)
    assert is_leap_year(1000)
    assert is_leap_year(1100)
    assert is_leap_year(1200)
    assert is_leap_year(1300)
    assert not is_leap_year(1751)
    assert is_leap_year(1752)
    assert not is_leap_year(1753)
    assert not is_leap_year(1800)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)
    assert not is_leap_year(2023)
    assert is_leap_year(2024)
    assert not is_leap_year(2025)
