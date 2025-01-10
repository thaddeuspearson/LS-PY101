import json

# Constants
MESSAGES_PATH = './calculator_messages.json'


# Helper functions
def load_messages(path=MESSAGES_PATH):
    with open(path, 'r') as f:
        return json.load(f)


def get_message_dict(lang='en'):
    message_dict = load_messages()
    return message_dict[lang]


def prompt(message):
    print(f"==> {message}")


def is_valid_number(num_str, **kwargs):
    try:
        float(num_str)
    except ValueError:
        return False
    return True


def is_valid_operation(operation, **kwargs):
    return operation in kwargs.get("valid_operations", [])


def get_valid_user_input(message, validation_func, **kwargs):
    prompt(message)
    user_input = input()
    while not validation_func(user_input, **kwargs):
        prompt(f"Invalid entry. {message}")
        user_input = input()
    return user_input


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
    messages = get_message_dict()

    prompt(messages["welcome"])

    while True:
        num_1 = get_valid_user_input(messages["number_prompt_1"],
                                     validation_func=is_valid_number)

        num_2 = get_valid_user_input(messages["number_prompt_2"],
                                     validation_func=is_valid_number)

        operation = get_valid_user_input(messages["operation_prompt"],
                                         validation_func=is_valid_operation,
                                         valid_operations=["1", "2", "3", "4"])

        result = calculate(num_1, num_2, operation)
        prompt(f"{messages['result']}: {result}")

        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_operation,
                                          valid_operations=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
