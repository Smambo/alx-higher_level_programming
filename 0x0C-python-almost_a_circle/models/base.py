#!/usr/bin/python3
"""Import modules."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return ([])
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """."""
        try:
            json_str = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            json_str = '[]'
        with open(cls.__name__+'.json', 'w', encoding="utf-8") as f:
            f.write(json_str)
