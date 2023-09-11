#!/usr/bin/python3
"""
Class object with public instance
methods that raise exception messages.
"""


class BaseGeometry:
    """Creates instance of class object."""
    def __init__(self):
        """Initialises class."""
        pass

    def area(self):
        """Raises Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
