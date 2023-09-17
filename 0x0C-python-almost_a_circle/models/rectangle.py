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
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height."""
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x attr."""
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y attr."""
        self.__y = value
