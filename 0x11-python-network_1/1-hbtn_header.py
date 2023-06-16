#!/usr/bin/python3
""""Inside the module"""
from sys import argv
from urllib import request


if __name__ == '__main__':
    url = argv[1]
    with request.urlopen(url) as response:
        print(dict(response.headers).get('X-Request-Id'))
