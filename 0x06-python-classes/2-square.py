#!/usr/bin/python3
"""Module doctstring."""


class Square:
    """Creates square object."""
    def __init__(self, size=0):
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = size
        """
        instantiates square
        Args:
            __size(int): size of the square
            size needs to be int and positive
        """
