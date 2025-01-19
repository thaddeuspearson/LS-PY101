"""
Write a function that takes a year as input and returns the century. The
return value should be a string that begins with the century number, and ends
with "st", "nd", "rd", or "th" as appropriate for that number.
"""


def century_suffix(cent):
    """Returns the correct century suffic for the given century.

    :cent (int): the given century
    :returns cent_suffix (str): the correct suffix for the given century.
    """
    if cent % 100 in [11, 12, 13]:
        return "th"
    elif cent % 10 == 1:
        return "st"
    elif cent % 10 == 2:
        return "nd"
    elif cent % 10 == 3:
        return "rd"
    else:
        return "th"


def century(year):
    """Returns a formatted string indicating the century of the given year.

    :year (int): the given year
    :returns (str): the formatted century string
    """
    cent = year // 100 if year % 100 == 0 \
        else (year + 100 - (year % 100)) // 100

    return f"{cent}{century_suffix(cent)}"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 26, the century function is defined with a single parameter, year.

On line 32, a ternary statement calculates the given year's century by
rounding up to the nearest century using modulo math, and retrieving the
century number with floor division.

On line 35, string interpolation concatenates the values of century and its
corresponding suffix with a call to the century_suffix helper funtion.

The century_suffix function is defined on line 8, with one parameter, cent.
The if/elif/else conditional block starting on line 14 checks for specific
edge cases, and uses modulo math to examine the final digits of century in
order to return the correct suffix.

Once the suffix is returned to century's execution context, the final
formatted century string is returned.
"""


# Test Cases
if __name__ == "__main__":
    assert century(2000) == "20th", "Should be True"
    assert century(2001) == "21st", "Should be True"
    assert century(1965) == "20th", "Should be True"
    assert century(256) == "3rd", "Should be True"
    assert century(5) == "1st", "Should be True"
    assert century(10103) == "102nd", "Should be True"
    assert century(1052) == "11th", "Should be True"
    assert century(1127) == "12th", "Should be True"
    assert century(11201) == "113th", "Should be True"
