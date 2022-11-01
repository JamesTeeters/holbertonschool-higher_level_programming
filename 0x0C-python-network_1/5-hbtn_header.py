#!/usr/bin/python3
"""display 'X-Requests-ID' using requests"""
from requests import get
import sys


if __name__ == '__main__':
    r = get(sys.argv[1]).headers.get("X-Request-Id")
    print(r)
