#!/usr/bin/python3
"""Almost a circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Created a subclass of rectangle square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
