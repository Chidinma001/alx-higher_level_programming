#!/usr/bin/python3
"""Inside the module"""
from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(r.text)
