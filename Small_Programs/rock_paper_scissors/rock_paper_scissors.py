"""
Classic rock / paper / scissors Game playable from the cmd line. Also supports
the lizard / spock variation as a tribute to The Big Bang Theory TV show
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_choice, get_random_choice)


# Constants
MESSAGES_PATH = './rock_paper_scissors_messages.json'
VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WIN_CONDITIONS = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }


def calculate_winner(player_choice, computer_choice, win_conditions):
    """Calculaters a winer for rock, paper, scissors, lizard spock (rpsls)

    :player_choice (str): the player's choice
    :computer_choice (str): the computer's choice
    :win_conditions (dict): the conditions necessary to win the game
    :returns winner (string): "player"/"computer"/"tie"
    """
    if computer_choice in win_conditions[player_choice]:
        winner = "player"
    elif player_choice == computer_choice:
        winner = "tie"
    else:
        winner = "computer"

    return winner


def main():
    """Driver function for the rock / paper / scissors game
    :returns (NoneType): None
    """
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages['welcome'])

    while True:
        choice_str = f"{messages["choice_prompt"]}: {', '.join(VALID_CHOICES)}"
        player_choice = get_valid_user_input(choice_str,
                                             validation_func=is_valid_choice,
                                             valid_choices=VALID_CHOICES)
        prompt(f"{messages['player_choice']}: {player_choice}")

        computer_choice = get_random_choice(VALID_CHOICES)
        prompt(f"{messages['computer_choice']}: {computer_choice}")

        winner = calculate_winner(player_choice, computer_choice,
                                  win_conditions=WIN_CONDITIONS)
        prompt(f"{messages['winner']}: {winner}")

        another_round = get_valid_user_input(messages["another_round"],
                                             validation_func=is_valid_choice,
                                             valid_choices=["y", "n"])
        if another_round == "n":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
