#!/usr/bin/env python3

from brain_games.scripts.get_random_number import random_number

SPECIFICATION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def game():

    question = random_number()
    current_answer = "yes" if question % 2 == 0 else "no"

    return question, current_answer
