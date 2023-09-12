#!/usr/bin/python3
"""
Below class defines a student.
"""


class Student:
    """Creates instance of class."""
    def __init__(self, first_name, last_name, age):
        """Initialises class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return ({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return (self.__dict__)
