#!/usr/bin/python3
"""Input Output"""


class Student:
    """make a student"""
    def __init__(self, first_name, last_name, age):
        """add attributes to student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self.attrs = attrs
        attr_list = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__:
                attr_list[i] = self.__dict__[i]
        return attr_list
