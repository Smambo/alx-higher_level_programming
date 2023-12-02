#!/usr/bin/python3
"""
Below script sends POST request to passed URL
using requests pkg
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
