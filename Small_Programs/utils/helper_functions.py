"""Helper functions to be used in the Small Programs Section of LS-PY101"""
import json


def load_messages(path):
    """Loads a json file from the given path

    :path (string): the filepath to the location of the json file
    :returns (dict): the deserialized json data loaded in a dictionary"""
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)


def get_message_dict(path, lang='en'):
    """Returns a dictionary with messages in the supported language
    from a given json file.

    :path (string): the path to the json file
    :lang (string): the selected language
    :returns (dict): the messages dictionary loaded in the given language
    """
    message_dict = dict(load_messages(path))
    return message_dict[lang]


def prompt(message):
    """Formats and prints a given message with ==>

    :message (str): the message to format and print
    :returns (NoneType): None
    """
    print(f"==> {message}")


def is_valid_number(num_str):
    """Validates if a given number (in string format) is a valid float.

    :num_str (str): a string representation of a number
    :returns (bool): True / False
    """
    try:
        float(num_str)
    except ValueError:
        return False
    return True


def is_valid_choice(operation, **kwargs):
    """Validates if a given choice (in string format) is in the 
    given valid_operations (passed into kwargs).

    :num_str (str): a string representation of a number
    :returns (bool): True / False
    """
    return operation in kwargs.get("valid_choice", [])


def get_valid_user_input(message, validation_func, **kwargs):
    """Gets user input, validated by the given validation function.

    :message (string): The message to prompt the user
    :validation_func (function): the function to validate the user input
    :returns user_input (string): The validated user input string
    """
    prompt(message)
    user_input = input().strip("$%")
    while not validation_func(user_input, **kwargs):
        prompt(f"Invalid entry. {message}")
        user_input = input().strip("$%")
    return user_input
