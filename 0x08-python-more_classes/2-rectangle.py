#!/usr/bin/python3
"""Below class defines a rectangle
with attributes.
"""


class Rectangle:
    """Creates rectangle object."""
    def __init__(self, width=0, height=0):
        """Initialises instance of rectangle
        Args:
            __width(int): width of rectangle.
            __height(int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width."""
        return self.__width  # private instance

    @property
    def height(self):
        """Retrieves height."""
        return self.__height  # private instance

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
        """Sets the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))
