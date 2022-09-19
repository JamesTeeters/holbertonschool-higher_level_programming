#!/usr/bin/python3
"""Input Output"""

import json


def load_from_json_file(filename):
    """create object from json"""
    with open(filename, 'w') as f:
        json.dump(filename, f)
