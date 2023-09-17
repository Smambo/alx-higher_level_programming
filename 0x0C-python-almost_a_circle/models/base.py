#!/usr/bin/python3
"""
Below class will be the base of
the other classes in this project.
"""


class Base:
    """Created instance of class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
