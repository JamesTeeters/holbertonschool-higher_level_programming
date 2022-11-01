#!/usr/bin/python3
"""I don't like pep8"""
import sys
from urllib import request


if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as f:
        print(f.headers['X-Request-Id'])
