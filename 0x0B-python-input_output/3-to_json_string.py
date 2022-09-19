#!/usr/bin/python3
"""Input Output"""


import json


def to_json_string(my_obj):
    """JSON"""
    json_object = json.dumps(my_obj)
    return (json_object)
