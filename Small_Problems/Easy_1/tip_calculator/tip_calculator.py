"""
Create a simple tip calculator. The program should prompt for a bill amount
and a tip rate. The program must compute the tip, then print both the tip
and the total amount of the bill. You can ignore input validation and assume
that the user will enter valid numbers.
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path as p
path.append(str(p(__file__).parent/'../../../Lesson_2/Small_Programs/utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_number, is_valid_choice)

# Constants
MESSAGES_PATH = './tip_calculator_messages.json'


def calculate_total_bill_and_tip(bill_amount, tip_percent):
    """Calculates the total bill and tip from a given bill amount and a tip 
    percentage.

    :bill_amount (float): the total of the bill (tax included)
    :tip_percent (float): the percent rate of the tip to be calculated
    :returns bill_total, tip_total (tuple): the total bill and total tip amount
    """
    bill_amount = float(bill_amount)
    tip_percent = float(tip_percent) * .01
    tip_total = round((bill_amount * tip_percent), 2)
    bill_total = bill_amount + tip_total
    return bill_total, tip_total


def main():
    """Main driver function"""
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages["welcome"])

    while True:
        bill_amount = get_valid_user_input(messages["bill_amount_prompt"],
                                           validation_func=is_valid_number)

        tip_percent = get_valid_user_input(messages["tip_percent_prompt"],
                                           validation_func=is_valid_number)

        bill_total, tip_total = calculate_total_bill_and_tip(bill_amount,
                                                             tip_percent)
        prompt(f"{messages['tip_total']}: ${tip_total:.2f}")
        prompt(f"{messages['bill_total']}: ${bill_total:.2f}")

        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_choice,
                                          valid_choices=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
