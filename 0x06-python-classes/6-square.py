#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """Creates square object."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square."""
        return self.__size

    @property
    def position(self):
        """Retrieves position of square."""
        return self.__position

    @size.setter
    def size(self, value):
        """
        Sets the size property
        size needs to be an int and positive
        """
        if type(value) is not int:
            raise (TypeError("size must be an integer"))
        if value < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Sets position property
        position must be tuple of 2 positive ints
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with '#'."""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
