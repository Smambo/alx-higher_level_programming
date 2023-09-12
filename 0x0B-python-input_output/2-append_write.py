#!/usr/bin/python3
"""
Below function appends string at end
of a text file and returns number of
chars added.
"""


def append_write(filename="", text=""):
    """Returns file with appended string."""
    with open(filename, 'a+', encoding="utf-8") as f:
        return (f.write(text))
