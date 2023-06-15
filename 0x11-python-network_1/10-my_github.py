#!/usr/bin/python3
"""Inside the module"""
from sys import argv
import requests


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    r_json = r.json()
    print(r_json.get('id') if r_json else None)
