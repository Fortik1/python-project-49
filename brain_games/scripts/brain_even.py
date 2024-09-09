#!/usr/bin/env python3

import prompt
# from ..engine import start_game
from get_random_number import main


def main():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    question = main()
    current_answer = "yes" if question % 2 == 0 else "no"

    print(f"question: {question}")

    user_answer = prompt.string(f"Your answer: ")

    if user_answer != current_answer:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{current_answer}'")
        print("Let's try again, !")
        return

    print("Congratulations, !")


if __name__ == '__main__':
    main()
