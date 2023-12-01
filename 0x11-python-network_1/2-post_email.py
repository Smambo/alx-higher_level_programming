#!/usr/bin/python3
"""Below script sends POST request to passed URL"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    param = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(param).encode('ascii')
    handler = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(handler) as response:
        page = response.read().decode('utf-8')
        print(page)
