#!/usr/bin/env python3
from brain_games.scripts.get_random_number import random_number

SPECIFICATION = "What is the result of the expression?"

max_index_operator = 2


def game():
    operators_array = ["+", "-", "*"]
    index_operator = random_number(max_index_operator)
    operator = operators_array[index_operator]
    random_number_one = random_number()
    random_number_two = random_number()
    question = f"{random_number_one} {operator} {random_number_two}"

    match operator:
        case "+":
            current_answer = random_number_one + random_number_two
        case "-":
            current_answer = random_number_one - random_number_two
        case "*":
            current_answer = random_number_one * random_number_two


    return question, str(current_answer)
