#!/usr/bin/python3
"""
Below function returns list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Returns list of attributes and methods"""
    my_list = []
    for x in dir(obj):
        my_list.append(x)
    return my_list
