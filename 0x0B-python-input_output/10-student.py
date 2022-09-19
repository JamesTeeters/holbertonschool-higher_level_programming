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
        if attrs == None:
            return self.__dict__
        attr_list = {}
        for i in attrs:
            if i in self.__dict__:
                attr_list[i] = self.__dict__
        return attr_list
