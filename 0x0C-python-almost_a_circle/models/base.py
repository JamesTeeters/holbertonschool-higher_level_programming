#!/usr/bin/python3
"""Almost a Circle"""
import json


class Base:
    """Making a class for Base Shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Attributes for Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)