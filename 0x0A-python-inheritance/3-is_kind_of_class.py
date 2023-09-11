#!/usr/bin/python3
"""
Below function returns bool if obj is
instance of specified class, or if obj
is instance of class inherited from
specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True is instance
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
