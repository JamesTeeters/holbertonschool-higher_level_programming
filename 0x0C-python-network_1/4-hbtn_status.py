#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
from requests import get


if __name__ == '__main__':
    status = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(status.text)))
    print("\t- content: {}".format(status.text))
