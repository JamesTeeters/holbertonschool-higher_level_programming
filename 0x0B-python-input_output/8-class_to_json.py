#!/usr/bin/python3
"""Input Output"""

import json


def class_to_json(obj):
    """dictionary description for JSON serialization of an object:"""
    return json.dumps(obj.__dict__)