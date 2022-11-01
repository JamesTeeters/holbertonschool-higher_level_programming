#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == '__main__':
    rqst = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(rqst) as rcved:
        url = rcved.read()
        print("Body Response:")
        print("/t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode("utf-8")))
