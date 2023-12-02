#!/usr/bin/python3
"""
Below script displays your id using the Github API
"""
from sys import argv
import requests


try:
    req = requests.get("https://api.github.com/user",
                       auth=(argv[1], argv[2]))
    print(req.json().get('id'))
except Exception:
    print("None")
