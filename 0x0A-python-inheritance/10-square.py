#!/usr/bin/python3
"""inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        """attributes of rectangle"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.width, self.height)
