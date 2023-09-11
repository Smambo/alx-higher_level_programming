#!/usr/bin/python3
"""
Below function returns bool after checking
if object is exactly an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """Returns True if exactly an instance
    otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
