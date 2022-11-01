#!/usr/bin/python3
"""Get github credentials from GitHub API, display id"""
import sys
from requests import get


if __name__ == '__main__':
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = get(url, auth=(user, pwd))
    print(r.json().get("id"))
