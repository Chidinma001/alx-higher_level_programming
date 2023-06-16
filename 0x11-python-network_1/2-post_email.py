#!/usr/bin/python3
"""Inside the module"""
from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    url = argv[1]
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
