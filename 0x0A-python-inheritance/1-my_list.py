#!/usr/bin/python3
"""
Below class object inherits from
a list and prints a sorted version
of the list
"""


class MyList(list):
    """Created class object."""
    def print_sorted(self):
        """prints sorted list."""
        print(sorted(self))
