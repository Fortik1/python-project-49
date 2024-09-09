#!/usr/bin/env python3
import random


def random_number():
    return random.randint(0, 100)


def main(quantity=1):
    random_numbers = []

    for _ in range(0, quantity):
        random_numbers.append(random_number())

    return random_numbers


if __name__ == "__main__":
    main()
