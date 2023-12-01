#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    body = resp.text
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(body)
