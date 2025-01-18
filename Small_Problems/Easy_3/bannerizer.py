"""
Write a function that takes a short line of text and prints it within a box.
"""


def print_in_box(title):
    """Returns a title wrapped in an ASCII character box.
    
    :title (str): the title to put in the banner box
    :returns banner (str): the formatted banner with title in the center.
    """
    title_len = len(title)
    line = f"+-{'-' * title_len}-+\n"
    padding = f"| {' ' * title_len} |\n"
    title_line = f"| {title} |\n"

    return line + padding + title_line + padding + line


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
On line 6, the print_in_box function is defined with one parameter, title.
When called with a string passed to title as an argument, a local variable
called title_len is initialized to the value of the length of the title.

On line 13, the local variable line is created and assigned to an f-string
that uses string interpolation to multiply a blank space char multiplied by
the length of the title and concatenate that to the rest of the string.

The same approach is taken for the local variables padding and title_line.
At the end of each line, a newline char is added.
On line 17, the formatted string is retuened using string concatenation.
"""


# Test Cases
if __name__ == "__main__":
    assert print_in_box('To boldly go where no one has gone before.') == (
        "+--------------------------------------------+\n"
        "|                                            |\n"
        "| To boldly go where no one has gone before. |\n"
        "|                                            |\n"
        "+--------------------------------------------+\n"
        )
