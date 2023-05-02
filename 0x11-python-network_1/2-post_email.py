#!/usr/bin/python3
"""
Python script that takes a URL and an email,
sends a POST request to the URL with the email as a
parameter, and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

my_data = urllib.parse.urllencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, my_data)
with urllib.request.urlopen(req) as response:
    response_body = response.read().decode('utf-8')
    print(response_body)
