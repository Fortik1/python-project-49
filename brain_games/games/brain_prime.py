#!/usr/bin/env python3
from brain_games.scripts.get_random_number import random_number

SPECIFICATION = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


def game():
    question = random_number()
    current_answer = "yes" if is_prime(question) else "no"


    return question, current_answer
