#!/usr/bin/python3
"""
Below script sends request to URL and displays value of variable
X-Request-Id in response header using requests pkg
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
