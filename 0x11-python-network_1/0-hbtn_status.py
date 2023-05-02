#!/usr/bin/python3
"""
Module to fetch URL using URLlib.
"""
import urllib.request

if __name__ == '__main__':
    req = urlib.request.Request("https://alx-intranet.hbtn.io/status")
    with urlib.request.urlopen(req) as response:
        body_of_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_of_response)))
        print("\t- content: {}".format(body_of_response))
        print("\t- utf8 content: {}".format(body_of_response.decode("utf-8")))
