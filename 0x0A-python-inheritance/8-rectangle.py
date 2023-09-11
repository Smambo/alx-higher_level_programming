#!/usr/bin/python3
"""
Below Rectangle class inherits from
BaseGeometry class.
"""


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


"""
Below is the rectangle class.
"""


class Rectangle(BaseGeometry):
    """Creates instance of class."""
    def __init__(self, width, height):
        """Initialises rectangle class."""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
