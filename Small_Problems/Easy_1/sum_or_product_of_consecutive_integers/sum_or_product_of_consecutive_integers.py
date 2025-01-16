"""
Write a program that asks the user to enter an integer greater than 0, then
asks whether the user wants to determine the sum or the product of all numbers
between 1 and the entered integer, inclusive.
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path as p
path.append(str(p(__file__).parent/'../../../Lesson_2/Small_Programs/utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_number, is_valid_choice)


MESSAGES_PATH = "./sum_or_product_of_consecutive_integers_messages.json"


def calculate_sum_or_product(target_int, sum_or_product_choice):
    """Calcualtes the sum or product from 1 until the given product

    :target_int (int): an integer value to sum or product until
    :sum_or_product (str): "sum"/"product" indicating which op to perform
    :returns result (int): the result of the chosen operation
    """
    values_list = list(range(1, target_int+1))
    match sum_or_product_choice:
        case "sum":
            result = sum(values_list)
        case "product":
            result = 1
            for num in values_list:
                result *= num
    return result


def main():
    """Main driver function"""
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages["welcome"])

    while True:
        input_integer = get_valid_user_input(messages["input_integer_prompt"],
                                             validation_func=is_valid_number)

        sum_or_product = get_valid_user_input(
                                           messages["sum_or_product_prompt"],
                                           validation_func=is_valid_choice,
                                           valid_choices=["sum", "product"])

        result = calculate_sum_or_product(int(input_integer), sum_or_product)

        prompt(f"{messages['result']}: {result}")
        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_choice,
                                          valid_choices=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
