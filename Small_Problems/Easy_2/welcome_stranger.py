"""
Create a function that takes 2 arguments, a list and a dictionary.
The list will contain 2 or more elements that, when joined with
spaces, will produce a person's name. The dictionary will contain
two keys, "title" and "occupation", and the appropriate values.
Your function should return a greeting that uses the person's full
name, and mentions the person's title.
"""
import sys


def greetings(name_list, occupation_dict):
    """Returns a welcome message stating name and occupation.

    :name_list (dict): a list of names to concatenate
    :occupation_dict (dict): contains the "title" : "occupation"
    """
    return (
        f"Hello, {' '.join(name_list)}!"
        f" Nice to have a {occupation_dict['title']}"
        f" {occupation_dict['occupation']} around."
    )


"""CODE EXPLAINATION
On line 12, the greetings function is defined with two parameters,
name_list and occupation_dict. Upon execution, with a list of strings
passed to name_list and a dictionary (containing a title to occupation
key, value pair) as arguments, this function uses string interpolation
with 3 f-strings concatenated together to return a formatted greeting.

Within the first f-string interpolation, the join method is called on
a space character, and concatenates the name strings in name list
together with a single space between each of them. In the second and
third f-strings, the interpolation uses bracket notation to access the
corresponding keys in occupation_dict, returning the values at each key
respectively. The f-string interpolation handles the coercion of each
returned value to a string representation, in order to be able to
perform the concatenation, and return the final concatenated string.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        # Test Cases
        GREETING = greetings(
            ["John", "Q", "Doe"],
            {"title": "Master", "occupation": "Plumber"}
        )
        assert GREETING == (
            "Hello, John Q Doe! Nice to have a Master Plumber around."
        )
    else:
        print(greetings())
