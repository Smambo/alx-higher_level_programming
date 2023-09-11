#!/usr/bin/python3
"""
Below class object which has a public
instance method.
"""


class BaseGeometry:
    """Creates instance of class object."""
    def __init__(self):
        """Initialises class."""
        pass

    def area(self):
        """Raises exception."""
        raise Exception("area() is not implemented")
