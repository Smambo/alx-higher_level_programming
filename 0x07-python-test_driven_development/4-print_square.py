#!/usr/bin/python3
"""Below function prints a
square with the character '#'.
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    print('\n'.join('#' * size for n in range(size)))
