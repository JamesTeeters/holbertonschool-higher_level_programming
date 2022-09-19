#!/usr/bin/python3
"""Input Output"""


import json


def from_json_string(my_str):
    """JSON"""
    json_object = json.loads(my_str)
    return (json_object)
