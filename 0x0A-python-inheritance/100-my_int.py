#!/usr/bin/python3
"""
Below class inherits from int.
"""


class MyInt(int):
    """Creates instance of class."""
    def __init__(self, value):
        """Initialises class."""
        self.value = value

    def __eq__(self, b):
        """Inverts operators again."""
        return (self.value != b)

    def __ne__(self, b):
        """Inverts operators again."""
        return (self.value == b)
