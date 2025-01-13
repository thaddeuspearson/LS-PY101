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
NUM_OF_ROUNDS = 5
WIN_CONDITIONS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}


def initialize_scorecard():
    """Initializes a scorecard to keep track of the wins from each round.

    :num_of_rounds (int): the number of rounds to be played in the game.
    :returns scorecard (dict): dict with player/computer keys, initialized to 0
    """
    scorecard = {
        "Player": 0,
        "Computer": 0,
        "round_number": 1,
    }
    return scorecard


def score_round(round_winner, scorecard):
    """Updates the given scorecard, and checks for win conditions.

    :round_winner (string): the winner of the round ("player"/"computer")
    :scorecard (dict): dict with player/computer keys, with the current scores
    :returns (str) game_winner: the winner of the overall game
    """
    game_winner = None
    scorecard[round_winner] += 1

    if scorecard[round_winner] > (NUM_OF_ROUNDS // 2) or \
       scorecard["round_number"] == NUM_OF_ROUNDS:
        game_winner = round_winner

    if not game_winner:
        scorecard["round_number"] += 1

    return game_winner


def calculate_round_winner(player_choice, computer_choice, win_conditions):
    """Calculaters a winer for rock, paper, scissors, lizard spock (rpsls).

    :player_choice (str): the player's choice
    :computer_choice (str): the computer's choice
    :win_conditions (dict): the conditions necessary to win the game
    :returns winner (string): "player" / "computer" / "tie"
    """
    if computer_choice in win_conditions[player_choice]:
        winner = "Player"
    elif player_choice == computer_choice:
        winner = "tie"
    else:
        winner = "Computer"

    return winner


def main():
    """Driver function for the rock / paper / scissors game
    :returns (NoneType): None
    """
    messages = get_message_dict(path=MESSAGES_PATH)
    prompt(messages['welcome'])

    scorecard = initialize_scorecard()

    while True:
        choice_str = f"{messages["choice_prompt"]}: {', '.join(VALID_CHOICES)}"
        player_choice = get_valid_user_input(choice_str,
                                             validation_func=is_valid_choice,
                                             valid_choices=VALID_CHOICES)
        prompt(f"{messages['player_choice']}: {player_choice}")

        computer_choice = get_random_choice(VALID_CHOICES)
        prompt(f"{messages['computer_choice']}: {computer_choice}")

        round_winner = calculate_round_winner(player_choice, computer_choice,
                                              win_conditions=WIN_CONDITIONS)
        if round_winner == "tie":
            prompt(f"{messages["tie_round"]}\n")
            continue

        game_winner = score_round(round_winner, scorecard)

        if game_winner:
            prompt(f"{messages["game_over"]} {scorecard['round_number']}. " +
                   f"{game_winner} wins!!!")
            play_again = get_valid_user_input(messages["another_game"],
                                              validation_func=is_valid_choice,
                                              valid_choices=["y", "n"])
            if play_again == "n":
                prompt(messages['goodbye'])
                break
        else:
            prompt(f"{messages['round_winner']} "
                   f"{scorecard['round_number'] - 1} is {round_winner}.")

        prompt(f"{messages['current_score']}:")
        prompt(f"Player: {scorecard['Player']} " +
               f"Computer: {scorecard['Computer']}\n")


if __name__ == "__main__":
    main()
