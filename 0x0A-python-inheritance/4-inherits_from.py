#!/usr/bin/python3
"""inheritance"""


def inherits_from(obj, a_class):
    """Return true if inherited from class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
