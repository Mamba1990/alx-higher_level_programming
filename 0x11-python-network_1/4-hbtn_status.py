#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    cont = resp.text
    print('Body response:')
    print('\t- type: {}'.format(type(cont)))
    print('\t- content: {}'.format(cont))
