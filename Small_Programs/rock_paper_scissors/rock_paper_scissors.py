from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import (get_message_dict, prompt, get_valid_user_input,
                              is_valid_number, is_valid_choice,
                              get_random_choice)


# Constants
MESSAGES_PATH = './rock_paper_scissors_messages.json'
VALID_CHOICES = ["rock", "paper", "scissors"]


def calculate_winner(player_choice, computer_choice):
    """Calculaters a winer for rock, paper, scissors

    :player_choice (str): the player's choice
    :computer_choice (str): the computer's choice
    :returns winner (string): "player"/"computer"/"tie"
    """
    if ((player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")):
        winner = "player"
    winner = "tie" if player_choice == computer_choice else "computer"
    return winner


def main():
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

        winner = calculate_winner(player_choice, computer_choice)
        prompt(f"{messages['winner']}: {winner}")

        another_round = get_valid_user_input(messages["another_round"],
                                             validation_func=is_valid_choice,
                                             valid_choices=["y", "n"])
        if another_round == "n":
            prompt("Thank you. Goodbye!")
            break


if __name__ == "__main__":
    main()
