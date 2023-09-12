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
        if attrs and isinstance(attrs, list) and
        all(isinstance(x, str) for x in attrs):
            return ({x: y for x, y in self.__dict__.items() for x in attrs})
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance."""
        if json:
            self.__dict__ = json
