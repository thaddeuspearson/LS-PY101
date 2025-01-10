import json

# Constants
MESSAGES_PATH = './mortgage_calculator_messages.json'


# Helper functions
def load_messages(path=MESSAGES_PATH):
    with open(path, 'r') as f:
        return json.load(f)


def get_message_dict(lang='en'):
    message_dict = load_messages()
    return message_dict[lang]


def prompt(message):
    print(f"==> {message}")


def is_valid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return False
    return True


def is_valid_operation(operation, **kwargs):
    return operation in kwargs.get("valid_operations", [])


def get_valid_user_input(message, validation_func, **kwargs):
    prompt(message)
    user_input = input().strip("$%")
    while not validation_func(user_input, **kwargs):
        prompt(f"Invalid entry. {message}")
        user_input = input().strip("$%")
    return user_input


def calculate_monthly_payment(loan_amount, apr, loan_duration):
    loan_amount = float(loan_amount)
    apr = float(apr)
    loan_duration = float(loan_duration)
    mir = (.01 * apr) / 12  # monthly interest rate
    return round(loan_amount * (mir / (1 - (1 + mir) ** (-loan_duration))), 2)


def main():
    # Load messages from json
    messages = get_message_dict()

    # Print a welcome banner.
    prompt(messages["welcome"])

    while True:
        # Ask the user for the loan amount.
        loan_amount = get_valid_user_input(messages["loan_amount_prompt"],
                                           validation_func=is_valid_number)

        # Ask the user for the annual percentage rate (APR).
        apr = get_valid_user_input(messages["apr_prompt"],
                                   validation_func=is_valid_number)

        # Ask the user for the loan duration (in months)
        loan_duration = get_valid_user_input(messages["loan_duration_prompt"],
                                             validation_func=is_valid_number)

        # Perform the operation on the two numbers.
        result = calculate_monthly_payment(loan_amount, apr, loan_duration)

        # Print the result to the terminal.
        prompt(f"{messages['monthly_payment']}: ${result}")

        # Ask if the user wants to perform another calculation.
        another_op = get_valid_user_input(messages["another_op"],
                                          validation_func=is_valid_operation,
                                          valid_operations=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
