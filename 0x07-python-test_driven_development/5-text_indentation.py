#!/usr/bin/python3
"""Function prints text with two lines
after each of these characters: `.`, `?` and `:`
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = 0
    for idx, val in enumerate(text):
        if val in '.?:':
            print(text[start:idx + 1].strip() + '\n')
            start = idx + 1
    if not start:
        print(text, end='')
    elif start is not len(text):
        print(text[start:idx + 1].strip(), end='')
