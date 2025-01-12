from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_number, is_valid_operation)


# Constants
MESSAGES_PATH = './mortgage_calculator_messages.json'


def calculate_monthly_payment(loan_amount, apr, loan_duration):
    loan_amount = float(loan_amount)
    apr = float(apr)
    loan_duration = float(loan_duration)
    mir = (.01 * apr) / 12  # monthly interest rate
    return round(loan_amount * (mir / (1 - (1 + mir) ** (-loan_duration))), 2)


def main():
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages["welcome"])

    while True:
        loan_amount = get_valid_user_input(messages["loan_amount_prompt"],
                                           validation_func=is_valid_number)

        apr = get_valid_user_input(messages["apr_prompt"],
                                   validation_func=is_valid_number)

        loan_duration = get_valid_user_input(messages["loan_duration_prompt"],
                                             validation_func=is_valid_number)

        result = calculate_monthly_payment(loan_amount, apr, loan_duration)
        prompt(f"{messages['monthly_payment']}: ${result}")

        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_operation,
                                          valid_operations=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
