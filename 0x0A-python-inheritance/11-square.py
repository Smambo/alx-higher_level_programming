#!/usr/bin/python3
"""BaseGeometry class below."""


class BaseGeometry:
    """Creates instance of class."""
    def area(self):
        """Raises Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Below is Rectangle class."""


class Rectangle(BaseGeometry):
    """Creates instance of class."""
    def __init__(self, width, height):
        """Initialises class."""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """Returns rectangle area."""
        return (self.__width * self.__height)

    def __str__(self):
        """Modifies str object."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


"""
Below class inherits from Rectangle class.
"""


class Square(Rectangle):
    """Creates instance of class."""
    def __init__(self, size):
        """Initialises rectangle."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Modifies str object."""
        return ("[Square {}/{}]".format(self.__size, self.__size))
