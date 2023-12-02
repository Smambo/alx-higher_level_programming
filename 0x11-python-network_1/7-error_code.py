#!/usr/bin/python3
"""
Below script sends request URL and displays body of response
or error codes using requests pkg
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
