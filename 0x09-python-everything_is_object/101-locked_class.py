#!/usr/bin/python3
"""Below class module prevents user from
dynamically creating new instance attributes
except if the new attribute is called 'first_name.
"""


class LockedClass:
    """Creates class object."""
    __slots__ = ['first_name']
