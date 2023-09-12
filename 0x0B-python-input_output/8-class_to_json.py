#!/usr/bin/python3
"""
Below function returns dictionary
description for json serialization
of an object.
"""


def class_to_json(obj):
    """Returns dict description."""
    return (obj.__dict__)
