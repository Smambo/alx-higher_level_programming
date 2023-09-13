#!/usr/bin/python3
"""
Below function inserts line of text to
a file, after each line containing
a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends lines."""
    with open(filename, 'r', encoding="utf-8") as f:
        line = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for text in line:
            f.write(text)
            if search_string in text:
                f.write(new_string)
