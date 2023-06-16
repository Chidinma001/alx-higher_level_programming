#!/usr/bin/python3
"""Inside the module"""
from sys import argv
import requests


if __name__ == '__main__':
    payload = {"q": argv[1] if len(argv) > 1 else ""}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=payload)
    res = r.json()
    try:
        if not res:
            print('No result')
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print('Not a valid JSON')
