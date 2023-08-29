#!/usr/bin/python3
"""Module docstring"""


class Square:
    """Creates square object"""
    def __init__(self, size=0):
        self.__size = size
        """Initialises size parameter
        Args:
            __size(int): size of square
        """
    @property
    def size(self):
        return self.__size
    """Retrieves size of square"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        if value < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = value
        """Sets theh size of square
        size must be an int and positive
        """
    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)
