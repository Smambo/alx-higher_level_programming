#!/usr/bin/python3
"""Module docstring"""


class Square:
    """creates square object"""
    def __init__(self, size=0):
        """Initialises instance of square
        Args:
            __size(int): size of square
            size must be int and positive
        """
        if type(size) is not int:
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = size

    def area(self):
        """Returns current square area."""
        return (self.__size ** 2)
