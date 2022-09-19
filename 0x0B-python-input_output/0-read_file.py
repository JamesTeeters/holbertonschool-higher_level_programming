#!/usr/bin/python3
"""Input Output"""


def read_file(filename=""):
    """open and read all line in file"""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
