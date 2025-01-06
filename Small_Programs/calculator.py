# Constants
VALID_OPERATIONS = ['1', '2', '3', '4']

# Helper functions
def prompt(message):
    print(f"==> {message}")

def is_valid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        prompt("invalid number entered. Try again")
        return False
    return True

def is_valid_operation(operation, valid_operations=VALID_OPERATIONS):
    return True if operation in valid_operations else False

# Print a welcome banner.
prompt('Welcome to Calculator!')

# Ask the user for the first number.
prompt("What's the first number?")
number1 = input()

while not is_valid_number(number1):
    number1 = input()

# Ask the user for the second number.
prompt("What's the second number?")
number2 = input()

while not is_valid_number(number2):
    number2 = input()

# Ask the user for an operation to perform.
prompt("What operation would you like to perform? \
       \n1) Add 2) Subtract 3) Multiply 4) Divide")

operation = input()

while not is_valid_operation(operation):
    prompt(f"Please enter one of these numbers: {', '.join(VALID_OPERATIONS)}.")
    operation = input()

# Perform the operation on the two numbers.
if operation == "1":
    output = int(number1) + int(number2)
elif operation == "2":
    output = int(number1) - int(number2)
elif operation == "3":
    output = int(number1) * int(number2)
elif operation == "4":
    output = int(number1) / int(number2)

# Print the result to the terminal.
prompt(f"The result is: {output}")
