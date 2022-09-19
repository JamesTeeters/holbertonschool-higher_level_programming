#!/usr/bin/python3
"""Input Output"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
