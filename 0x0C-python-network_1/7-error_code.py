#!/usr/bin/python3
"""error handeling with request"""
import sys
from requests import get


if __name__ == '__main__':
    r = get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
