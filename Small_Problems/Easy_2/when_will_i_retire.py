"""
Build a program that displays when the user will retire and
how many years they have to work until retirement.
"""
import sys
from datetime import datetime


def get_years_until_retirement_str(curr_age="", retirement_age=""):
    """Returns the number of years until retirement string for the user.
    
    :curr_age (str): current age of the user
    :retirement_age (str): the age the user wants to be to retire
    :returns retirement_str (str): The formatted message to display
    """
    if not curr_age:
        curr_age = input("What is your age? ")
    if not retirement_age:
        retirement_age = input("At what age would you like to retire? ")

    curr_year = str((datetime.now()).year)
    years_to_go = int(retirement_age) - int(curr_age)
    retirement_year = int(curr_year) + years_to_go

    return (f"It's {curr_year}. You will retire in {retirement_year}.\n"
            f"You have only {years_to_go} years of work to go!")


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 6, we import datetime from the datetime module. Then on line 9, the
get_years_until_retirement_str is defined with two parameters, curr_age and
retirement_age.

The first two if conditional blocks check to see if curr_age and retirement_age
have had any arguments pased to them during execution, and if not, they prompt
the user with distinct calls to the built-in function input().

On line 21, local variable current_year is assigned to the value of the current
year using the datetime.now() function, (and accessing the .year property)from
the datetime module. On line 22, years_to_go is calculated by casting the
retirement_age and curr_age arguments, and assigning the result to years_to_go.
The retirement_year is calculated from adding yeare_to_go to the integer
representation of curr_year.

Finally, on line 25, string interpolation is used to insert the necessary
variables into the f-string that is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert get_years_until_retirement_str(30, 70) == (
                f"It's {(datetime.now()).year}. You will retire in "
                f"{(datetime.now()).year + 40}.\n"
                "You have only 40 years of work to go!")
    else:
        print(get_years_until_retirement_str())
