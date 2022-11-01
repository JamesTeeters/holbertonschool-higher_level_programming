#!/usr/bin/python3
"""I don't like pep8"""
import sys
import urllib.request


if __name__ == '__main__':
    rqst = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(rqst) as rcved:
        print(rcved.headers['X-Request-Id'])
