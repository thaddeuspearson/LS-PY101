"""
Write a program that asks for user's name, then greets the user.
If the user appends a ! to their name, the computer will yell the 
greeting (print it using all uppercase).
"""


def greet_user(input_str=""):
    """Greets a user, either via an input string, or user input
    from the cmd line.

    :input_str (str): an optional input string
    :returns (str): the greeting to send to the user
    """
    if not input_str:
        input_str = input("What is your name?")

    if input_str.endswith("!"):
        return f"HELLO {input_str.upper()} WHY ARE WE YELLING?"
    return f"Hello {input_str}."


"""CODE EXPLAINATION
On line 8, a function greet_user is defined with a single parameter
input_str, which has a default value of an empty string.

In the case no string is passed as an argument to input_str, the user
is prompted to enter their name from the command line. This condition
is checked on line 15, and inout_str is reassigned to the result of
calling the input function, which returns the user input as a string.

The next if conditional statement checks to see if the input_str ends
with a "!". if it does, the greeting is returned in all caps, and uses
string interpolation within the context of an f-string to uppercase the
users name with .upper. If the if statement evaluates to false, the
normal greeting is interpolated within a differnt f-string, and the
greeting is returned.
"""


# Test Cases
if __name__ == "__main__":
    assert greet_user("Sue") == "Hello Sue."
    assert greet_user("Bob!") == "HELLO BOB! WHY ARE WE YELLING?"
