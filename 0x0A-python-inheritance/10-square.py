#!/usr/bin/python3
"""
Below class
inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates instance of class."""
    def __init__(self, size):
        """Initialises rectangle."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
