#!/usr/bin/python3
"""Input Output"""
def read_file(filename=""):
    with open (filename, 'r') as fi:
        for line in fi:
            print (line, end='')
