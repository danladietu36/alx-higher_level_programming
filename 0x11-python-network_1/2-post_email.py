#!/usr/bin/python3
"""
Python script that takes a URL and an email,
sends a POST request to the URL with the email as a
parameter, and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    my_data = urllib.parse.urlencode(email_value).encode('ascii')
    req = urllib.request.Request(url, my_data)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
