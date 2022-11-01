#!/usr/bin/python3
"""POST'email' using request"""
import sys
from requests import post

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    r = post(sys.argv[1], data)
    print(r.text)
