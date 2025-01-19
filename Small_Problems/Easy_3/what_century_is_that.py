"""
Write a function that takes a year as input and returns the century. The
return value should be a string that begins with the century number, and ends
with "st", "nd", "rd", or "th" as appropriate for that number.
"""


def century(year):
    """Returns a formatted string indicating the century of the given year.

    :year (int): the given year
    :returns cent_str (str): the formatted century string
    """
    cent = year // 100 if year % 100 == 0 \
        else (year + 100 - (year % 100)) // 100

    cent_str = str(cent)

    if cent % 100 in range(4, 21):
        return cent_str + "th"
    elif cent % 10 == 1:
        return cent_str + "st"
    elif cent % 10 == 2:
        return cent_str + "nd"
    elif cent % 10 == 3:
        return cent_str + "rd"
    else:
        return cent_str + "th"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 8, the century function is defined with a single parameter, year.
On line 14, a ternary statement calculates the given year's century by
rounding up to the nearest century using modulo math, and retrieving the
century number with floor division.

On line 17, the local variable century_str is instantiated with the coerced
value of century assigned as it's value.

The if/elif/else conditional block starting on line 19 checks for specific
edge cases, and uses modulo math to examine the final digits of century in
order to concatenate the correct suffix to century_str and return it.
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
