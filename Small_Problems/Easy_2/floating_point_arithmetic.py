"""
Write a program that prompts the user for two positive numbers
(floating-point), then prints the results of the following
operations those two numbers: addition, subtraction, product,
quotient, floor quotient, remainder and power. Do not worry about
validating the input.
"""
import sys


OPERATORS = ['+', '-', '*', '/', '//', '%', '**']


def floating_point_arithmetic(input_num_1="", input_num_2=""):
    """Returns all mathematical oerations on the given two numbers.

    :input_num_1 (float): the first operand
    :input_num_2 (float): the second operand
    :returns (str): formatted string with the result of math operations
    """
    if not input_num_1:
        input_num_1 = input("==> Enter the first number: ")
    if not input_num_2:
        input_num_2 = input("==> Enter the second number: ")

    return_str = ""

    for op in OPERATORS:
        result = eval(f"{input_num_1} {op} {input_num_2}")
        return_str += f"==> {input_num_1} {op} {input_num_2} = {result}\n"

    return return_str


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 11, a constant variable is assigned to a list containing all of
the math operators in string representation.

On line 14, the floating_point_arithmetic function is defined with two
parameters, input_num_1, and input_num_2. Both parameters have default
values of empty strings.

The first two if statements starting on line 21 check to see if any
arguments were given to the parameters when the function was called.
If not, the input built-in function assigns input_num_1 and input_num_2
to the values given by the user at the command line.

On line 26, a local variable return_str is initialized as an empty string.

On line 28, a for loop is declared to loop through the list of operators.
The loop uses string interpolation combined with the eval statement to craft
the formatted strings with the correct result of the math operation. a newline
character is added at the end to make sure each math operation displays on a
separate line. Finally the interpolated string is concatenated to the
return_str variable, and at the conclusion of the loop is returned on line 32.
"""


if __name__ == "__main__":
    # Test Cases
    args = sys.argv[1:]
    if args and args[0] == "test":
        OUTPUT = (
            "==> 3.141529 + 2.718282 = 5.859811\n"
            "==> 3.141529 - 2.718282 = 0.42324699999999993\n"
            "==> 3.141529 * 2.718282 = 8.539561733178\n"
            "==> 3.141529 / 2.718282 = 1.1557038600115808\n"
            "==> 3.141529 // 2.718282 = 1.0\n"
            "==> 3.141529 % 2.718282 = 0.42324699999999993\n"
            "==> 3.141529 ** 2.718282 = 22.45792517468373\n"
        )
        assert floating_point_arithmetic(3.141529, 2.718282) == OUTPUT
    else:
        print(floating_point_arithmetic())
