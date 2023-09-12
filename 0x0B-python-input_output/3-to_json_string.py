#!/usr/bin/python3
"""Import json module."""
import json


"""
Below function returns JSON
representation of an object.
"""


def to_json_string(my_obj):
    """Serializies string object."""
    return (json.dumps(my_obj))
