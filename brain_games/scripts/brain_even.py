#!/usr/bin/env python3

import prompt
import random


def main():
    step_games = 0

    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    while step_games < 3:
        step_games += 1
        question = random.randint(0, 100)
        current_answer = "yes" if question % 2 == 0 else "no"

        print(f"question: {question}")

        user_answer = prompt.string(f"Your answer: ")

        if user_answer != current_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{current_answer}'")
            print("Let's try again, Bill!")
            return

    print("Congratulations, Bill!")


if __name__ == '__main__':
    main()
