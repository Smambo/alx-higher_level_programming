#!/usr/bin/python3
"""
Below class inherits from Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Created instance of class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialises class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Modifies the str object."""
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x, self.y, self.size))
