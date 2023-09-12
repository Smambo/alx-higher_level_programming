#!/usr/bin/python3
"""
Below function writes a string to a
text file and returns number of chars
written.
"""


def write_file(filename="", text=""):
    """Writes string to text file."""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
