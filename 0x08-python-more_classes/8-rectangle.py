#!/usr/bin/python3
"""Class module defines a
rectangle with attributes.
"""


class Rectangle:
    """Creates rectangle class object."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialises instance of rectangle
        Args:
            __width(int): width of rectangle
            __height(int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width."""
        return self.__width  # private instance

    @property
    def height(self):
        """Retrieves height."""
        return self.__height  # private instance

    @width.setter
    def width(self, value):
        """Sets width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle
        based on area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Modifies str object."""
        if self.width == 0 or self.height == 0:
            return ""
        return ('\n'.join("{}".format(self.print_symbol * self.width
                for n in range(self.height))))

    def __repr__(self):
        """Modifies repr object."""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Modifies del object."""
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
