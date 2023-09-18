#!/usr/bin/python3
"""Import modules."""
import json
import os.path


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns json representation og json_string.
        """
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes json string representation of list to a file.
        """
        try:
            json_str = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            json_str = '[]'
        with open(cls.__name__+'.json', 'w', encoding="utf-8") as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns instance with all attributes already set.
        """
        if cls.__name__ == "Square":
            new = cls(1)
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if new:
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns list of instances.
        """
        if not os.path.isfile(cls.__name__ + '.json'):
            return ([])
        else:
            with open(cls.__name__ + '.json', 'r', encoding="utf-8") as f:
                dict_list = cls.from_json_string(f.read())
            return ([cls.create(**dic) for dic in dict_list])
