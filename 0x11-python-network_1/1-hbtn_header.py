#!/usr/bin/python3
"""Module that that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import sys
import urlib.request


if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
