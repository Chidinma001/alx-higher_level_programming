#!/usr/bin/python3
"""Inside the module"""
from sys import argv
import requests


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    r_json = r.json()
    try:
        for ele in r_json[:10]:
            print('{}: {}'.format(ele.get('sha'), ele.get('commit').get('author').get('name')))
    except IndexError:
        pass
