#!/usr/bin/python3
"""Import json module."""
import json


"""
Below function writes an object to a
text file, using json representation
"""


def save_to_json_file(my_obj, filename):
    """uses json to write to file."""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
