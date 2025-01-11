"""
Build a program that asks the user to enter the length and width of a room,
in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""


# Helper functions
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


def get_valid_user_input(message, validation_func=is_valid_number):
    """Gets user input, validated by the given validation function.

    :message (string): The message to prompt the user
    :validation_func (function): the function to validate the user input
    :returns user_input (string): The validated user input string
    """
    print(message)
    user_input = input()
    while not validation_func(user_input):
        print(f"Invalid entry. {message}")
        user_input = input()
    return user_input


def get_square_meters(length, width):
    """Calculates square meters from the given length and width.

    :length (float): the length of the area
    :width (float): the width of the area
    :returns (float): the square meters of the area
    """
    return length * width


def convert_square_meters_to_square_feet(square_meters):
    """Converts square meters to square feet

    :square_meters (float): the square meters to convert to square feet
    :returns (float): square meters converted to square feet
    """
    return square_meters * 10.7639


def print_area_in_meters_and_feet(square_meters, square_feet):
    """Prints the area of the given room in meters and feet

    :square_meters (float): the area in square meters
    :square_feet (float): the area in square feet
    :returns (NoneType): None
    """
    print("The area of the room is:")
    print(f"\t{square_meters} square meters")
    print(f"\t{square_feet} square feet")


def main():
    print("Welcome. How big is the room?")
    length_message = "Please enter the length of the room in meters."
    length_in_meters = get_valid_user_input(length_message)

    width_message = "Please enter the length of the room in meters."
    width_in_meters = get_valid_user_input(width_message)

    square_meters = get_square_meters(length_in_meters, width_in_meters)
    square_feet = convert_square_meters_to_square_feet(square_meters)

    print_area_in_meters_and_feet(square_meters, square_feet)


if __name__ == "__main__":
    main()
