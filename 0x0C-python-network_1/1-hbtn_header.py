#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
import sys
import urllib.request


rqst = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(rqst) as rcved:
    print(rcved.headers['X-Request-Id'])
