"""
Write a function that determines the mean (average) of the three scores passed
to it, and returns the letter associated with that grade.
"""


def get_grade(score_1, score_2, score_3):
    """Calculates the average of the three grades given, and returns the
    letter grade.

    :score_1 (int): the first score
    :score_2 (int): the second score
    :score_3 (int): the third score
    :returns (str): The letter grade of the average of the scores
    """
    average = (score_1 + score_2 + score_3) // 3

    if 90 <= average:
        return 'A'
    elif 80 <= average:
        return 'B'
    elif 70 <= average:
        return 'C'
    elif 60 <= average:
        return 'D'
    else:
        return 'F'


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
The function get_grade is defined on line 7, with 3 parameters, score_1,
score_2, and score_3. On line 16, the local variable average is created
and assigned to the value of the average of the three score arguments
passed during execution, floor divided by 3.

The if/elif/else conditional block beginning on line 18 then uses
short-circuiting by comparing average to each letter grade's minimal score,
with the highest score at the top of the block, and the least at the bottom.
This control flow order guarentees that the correct letter grade will be
returned in the assiciated if/elif/else statement.
"""


# Test Cases
if __name__ == "__main__":
    assert get_grade(95, 90, 93) == "A", "Should be True"
    assert get_grade(50, 50, 95) == "D", "Should be True"
