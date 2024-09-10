#!/usr/bin/env python3
from brain_games.scripts.get_random_number import random_number


SPECIFICATION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def game():

    random_number_one = random_number()
    random_number_two = random_number()
    question = f"{random_number_one} {random_number_two}"
    current_answer = gcd(random_number_one, random_number_two)

    return question, str(current_answer)
