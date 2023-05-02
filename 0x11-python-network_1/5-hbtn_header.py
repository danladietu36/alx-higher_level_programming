#!/usr/bin/python3
"""
Python script that takes a URL, sends a request to the
URL, and displays the value of the X-Request-Id
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)
    requestId = response.headers.get('X-Request-Id')

    print(requestId)
