#!/usr/bin/python3
"""inheritance"""


class BaseGeometry:
    """created empty class"""
    def area(self):
        """add attributes to class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
