#!/usr/bin/python3
"""The below class defines a rectangle
with attributes.
"""


class Rectangle:
    """Creates rectangle class object."""
    def __init__(self, width=0, height=0):
        """Initialises instance of rectangle
        Args:
            __width(int): width of rectangle
            __height(int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
