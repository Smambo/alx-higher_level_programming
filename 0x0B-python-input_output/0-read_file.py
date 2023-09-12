#!/usr/bin/python3
"""
Below function reads a text file
and prints it to stdout.
"""


def read_file(filename=""):
    """Reads text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
