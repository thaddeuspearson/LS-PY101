import json

# Constants
MESSAGES_PATH = './tip_calculator_messages.json'


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


def calculate_total_bill_and_tip(bill_amount, tip_percent):
    bill_amount = float(bill_amount)
    tip_percent = float(tip_percent) * .01
    tip_total = round((bill_amount * tip_percent), 2)
    bill_total = bill_amount + tip_total
    return bill_total, tip_total


def main():
    messages = get_message_dict()
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
                                          validation_func=is_valid_operation,
                                          valid_operations=["1", "2"])
        if another_op == "2":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
