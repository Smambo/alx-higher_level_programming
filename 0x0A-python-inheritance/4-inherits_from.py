#!/usr/bin/python3
"""
Below function checks if object is instance of
a class that is inherited from specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if isinstance
    otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
