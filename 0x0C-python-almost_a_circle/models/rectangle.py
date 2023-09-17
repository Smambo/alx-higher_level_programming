#!/usr/bin/python3
"""
Below class inherits from Base class.
"""
from models.base import Base


class Rectangle(Base):
    """Created instance of class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator(self, name, value):
        """Validates other methods."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @property
    def x(self):
        """Retrieves x attr."""
        return self.__x

    @property
    def y(self):
        """Retrieves y attr."""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width."""
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height."""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x attr."""
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y attr."""
        self.validator("y", value)
        self.__y = value
