#!/usr/bin/python3
"""Input Output"""


def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
