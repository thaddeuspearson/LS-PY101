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
