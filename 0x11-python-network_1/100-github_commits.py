#!/usr/bin/python3
"""
Takes 2 arguments in order to list 10 commits (from the most
recent to oldest) of the repository "rails" by the user "rails".
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repoName = sys.argv[1]
        user_name = sys.argv[2]
        commmitsUrl = "https://api.github.com/repos/{}/{}/commits" \
            .format(user_name, repoName)
        resp = requests.get(commmitsUrl)
        jsonObj = resp.json()
        for j, obj in enumerate(jsonObj):
            if j == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
