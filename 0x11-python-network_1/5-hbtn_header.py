#!/usr/bin/python3
"""Inside the module"""
from sys import argv
import requests


if __name__ == '__main__':
    url = argv[1]
    print(requests.get(url).headers.get('X-Request-Id'))
