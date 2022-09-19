#!/usr/bin/python3
"""Input Output"""


def write_file(filename="", text=""):
    """Write in Text file"""
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)
