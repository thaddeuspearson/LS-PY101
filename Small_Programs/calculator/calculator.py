from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_number, is_valid_choice)

# Constants
MESSAGES_PATH = './calculator_messages.json'


def calculate(num_1, num_2, operation):
    match operation:
        case "1":
            output = float(num_1) + float(num_2)
        case "2":
            output = float(num_1) - float(num_2)
        case "3":
            output = float(num_1) * float(num_2)
        case "4":
            output = float(num_1) / float(num_2)
    return output


def main():
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages["welcome"])

    while True:
        num_1 = get_valid_user_input(messages["number_prompt_1"],
                                     validation_func=is_valid_number)

        num_2 = get_valid_user_input(messages["number_prompt_2"],
                                     validation_func=is_valid_number)

        operation = get_valid_user_input(messages["operation_prompt"],
                                         validation_func=is_valid_choice,
                                         valid_choices=["1", "2", "3", "4"])

        result = calculate(num_1, num_2, operation)
        prompt(f"{messages['result']}: {result}")

        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_choice,
                                          valid_choices=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
