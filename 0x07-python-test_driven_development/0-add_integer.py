#!/usr/bin/python3
"""
This function adds 2 integers
Returns an integer which is
the addition of a and b
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
