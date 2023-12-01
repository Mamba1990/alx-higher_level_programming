#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
The first argument will be your username.
The second argument will be your password (in your case, a personal
access token as password).
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    resp = requests.get(url, auth=HTTPBasicAuth(user_name, pass_word))
    jsonObj = resp.json()
    print(jsonObj.get("id"))
