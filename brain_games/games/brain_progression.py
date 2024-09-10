#!/usr/bin/env python3
from brain_games.scripts.get_random_number import random_number

SPECIFICATION = "What number is missing in the progression?"

max_length_progression = 10


def game():
    progression = random_number()
    question = range(0, max_length_progression, progression)
    miss_number_index = random_number(max_length_progression) - 1
    current_answer = question[miss_number_index]
    question[miss_number_index] = "..."
    print(question)

    return question, str(current_answer)
