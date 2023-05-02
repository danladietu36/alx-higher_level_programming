#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    url_response = requests.get(url)
    response_body = url_response.json()

    print('Body response:')
    print('\t- type: {}'.format(type(response_body)))
    print('\t- content: {}'.format(response_body))
