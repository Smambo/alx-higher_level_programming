#!/usr/bin/python3
"""
Below script sends request URL and displays body of response
or error codes
"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))
