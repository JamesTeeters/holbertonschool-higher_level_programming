#!/usr/bin/python3
"""Almost a Circle"""


from http.client import BadStatusLine


class Base:
    """Making a class for Base Shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Attributes for Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
