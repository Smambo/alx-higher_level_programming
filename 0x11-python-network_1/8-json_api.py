#!/usr/bin/python3
"""
Below script takes in a letter and sends POST request to a url
with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        if req.json():
            print("[{}] {}".format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
