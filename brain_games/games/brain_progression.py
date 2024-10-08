#!/usr/bin/env python3
from brain_games.scripts.get_random_number import random_number

SPECIFICATION = "What number is missing in the progression?"

max_length_progression = 10
max_progression = 25
min_progression = 1


def create_array(start, progression):
    end_number = start + (max_length_progression * progression)
    question = []
    for number in range(start, end_number, progression):
        question.append(number)
    return question


def game():
    start_number = random_number()
    progression = random_number(max_progression, min_progression)
    question = create_array(start_number, progression)
    miss_number_index = random_number(max_length_progression - 1)
    current_answer = question[miss_number_index]
    question[miss_number_index] = ".."

    return " ".join(map(str, question)), str(current_answer)
