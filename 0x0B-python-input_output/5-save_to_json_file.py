#!/usr/bin/python3
"""Input Output"""

import json


def save_to_json_file(my_obj, filename):
    """write from jason to python"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
