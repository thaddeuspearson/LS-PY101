"""
Create a simple madlib program that prompts for a noun, a verb, an adverb, and
an adjective, and injects them into a story that you create.
"""
import sys


def create_madlib(noun='', verb='', adjective='', adverb=''):
    """Returns a madlib string with the corresponding noun, verb, adjective,
    and adverb placed into the story.

    :noun (str): the noun of the madlib
    :verb (str): the verb of the madlib
    :adjective (str): the adjective of the madlib
    :adverb (str): the adverb of the madlib
    :returns madlib (str): the final story with the included elements above
    """
    if not noun:
        noun = input("Enter a noun: ")
    if not verb:
        verb = input("Enter a verb: ")
    if not adjective:
        adjective = input("Enter an adjective: ")
    if not adverb:
        adverb = input("Enter an adverb: ")

    return (
        f"Do you {verb} your {adjective} {noun} {adverb}? That's "
        f"hilarious!\nThe {adjective} {noun} {verb}s {adverb} over the "
        f"lazy {noun}.\nThe {noun} {adverb} {verb}s up to Joe's {adjective} "
        f"turtle.\n")


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION

"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert create_madlib("dog", "walk", "blue", "quickly") == (
            "Do you walk your blue dog quickly? That's hilarious!\n"
            "The blue dog walks quickly over the lazy dog.\n"
            "The dog quickly walks up to Joe's blue turtle.\n"
            )
    else:
        print(create_madlib())
