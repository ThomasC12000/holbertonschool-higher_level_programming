#!/usr/bin/python3
'''function that prints a square with a given size'''


def print_square(size):
    '''Prints a square with # character'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size > 0:
        raise TypeError("size must be an integer")
    for print_square in range(size):
        print("#" * size)
