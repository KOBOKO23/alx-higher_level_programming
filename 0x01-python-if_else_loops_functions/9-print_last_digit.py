#!/usr/bin/python3


def print_last_digit(num):
    """Print the last digit of a number and return it."""
    print(abs(num) % 10, end="")
    return (abs(num) % 10)
