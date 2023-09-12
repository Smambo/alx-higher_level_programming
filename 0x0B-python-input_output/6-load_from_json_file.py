#!/usr/bin/python3
"""Import json."""
import json


"""
Below function creates object
from json file.
"""


def load_from_json_file(filename):
    """Creates an object."""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
