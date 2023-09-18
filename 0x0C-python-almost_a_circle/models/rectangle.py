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

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute."""
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dict representation of Rectangle."""
        my_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
        return my_dict

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

    def area(self):
        """Returns rectangle area."""
        return (self.width * self.height)

    def display(self):
        """
        Prints rectangle to stdout
        using '#'.
        """
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
              for times in range(self.height)), end="")

    def __str__(self):
        """Modifies str obj."""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width, self.height))
