#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user


def start_game(game_rules):
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")

    max_step_game = 3

    print(game_rules.SPECIFICATION)

    for _ in range(max_step_game):
        question, current_answer = game_rules.game()
        print(f"question: {question}")

        user_answer = prompt.string("Your answer: ")

        if user_answer == current_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{current_answer}'")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
