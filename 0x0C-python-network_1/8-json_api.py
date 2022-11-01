#!/usr/bin/python3
"""POST to API with letter as parameter"""
import sys
from requests import post


if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    p = post("http://0.0.0.0:5000/search_user", data)
    try:
        if p.json():
            print("[{}] {}".format(p.json()["id"], p.json()["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
