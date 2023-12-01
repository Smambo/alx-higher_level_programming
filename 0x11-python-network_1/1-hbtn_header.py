#!/usr/bin/python3
"""
Below script takes URL, sends request to URL and displays
value of X-Requests-Id variable found in header of response
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
