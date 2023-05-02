#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8), while handling
urllib.error.HTTPError exceptions.
"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.Request(url) as response:
            response_body = response_body.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
