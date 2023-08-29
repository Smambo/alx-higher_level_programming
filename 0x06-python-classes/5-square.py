#!/usr/bin/python3
"""Module docstring"""


class Square:
    """Creates square object."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)
    """Returns size of square"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        if value < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = value
    """Sets the size of the square"""
    def area(self):
        return (self.__size ** 2)
    """Returns the current square area."""
    def my_print(self):
        """Prints in stdout the square with '#'"""
        if self.size:
            for i in range(self.size):
                print("#" * self.size, end='')
                print()
        else:
            print()
