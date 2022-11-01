#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as f:
        url = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode("utf-8")))
