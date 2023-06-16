#!/usr/bin/python3
"""Inside the module"""
from sys import argv
from urllib import error, request


if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('ascii'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
