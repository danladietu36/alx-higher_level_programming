#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package.
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    url_response = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(url_response)))
    print('\t- content: {}'.format(url_response))
