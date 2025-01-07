import json

# Constants
VALID_OPERATIONS = ['1', '2', '3', '4']


# Helper functions
def get_message_dict(path='calculator_messages.json'):
    with open(path, 'r') as f:
        return json.load(f)


def prompt(message):
    print(f"==> {message}")


def is_valid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return False
    return True


def get_valid_user_input(message, validation_func, **kwargs):
    prompt(message)
    user_input = input()
    while not validation_func(user_input, **kwargs):
        prompt(f"Invalid entry. {message}")
        user_input = input()
    return user_input


def is_valid_operation(operation, valid_operations=VALID_OPERATIONS):
    return operation in valid_operations


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
    # Print a welcome banner.
    prompt('Welcome to Calculator!')

    while True:
        # Ask the user for the first number.
        num_1 = get_valid_user_input("What's the first number?",
                                     is_valid_number)

        # Ask the user for the second number.
        num_2 = get_valid_user_input("What's the second number?",
                                     is_valid_number)

        # Ask the user for an operation to perform.
        operation = get_valid_user_input("What operation do you want to do?"
                                         "\n1) Addition  2) Subtraction  "
                                         "3) Multiplication  4) Division",
                                         is_valid_operation)

        # Perform the operation on the two numbers.
        output = calculate(num_1, num_2, operation)

        # Print the result to the terminal.
        prompt(f"The result is: {output}")

        # Ask if the user wants to perform another calculation
        another_calculation = get_valid_user_input("Would you like to perform "
                                                   "another calculation?\n"
                                                   "1) Yes  2) No ",
                                                   is_valid_operation,
                                                   valid_operations=["1", "2"])
        if another_calculation == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
