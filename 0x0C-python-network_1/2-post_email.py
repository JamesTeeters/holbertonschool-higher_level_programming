#!/usr/bin/python3
"""send POST request"""
import sys
from urllib import request
from urllib import parse


if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('ascii')
    with request.urlopen(sys.argv[1], data) as f:
        var = f.read().decode('utf-8')
        print(var)
