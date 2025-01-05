# Print a welcome banner.
print('Welcome to Calculator!')

# Ask the user for the first number.
print("What's the first number?")
number1 = input()

# Ask the user for the second number.
print("What's the second number?")
number2 = input()

# Ask the user for an operation to perform.
print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
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
print(f"The result is: {output}")