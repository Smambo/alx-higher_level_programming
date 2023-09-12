#!/usr/bin/python3
"""Import json module."""
import json


"""
Function returns an object
represented by json string.
"""


def from_json_string(my_str):
    """Deserializes json object."""
    return (json.loads(my_str))
