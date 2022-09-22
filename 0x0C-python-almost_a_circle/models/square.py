#!/usr/bin/python3
"""Almost a circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Created a subclass of rectangle square"""
    def __init__(self, size, x=0, y=0, id=None):
        """add attribute to Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        self.__width = value
        self.__heigth = value
