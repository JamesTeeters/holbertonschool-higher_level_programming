#!/usr/bin/python3
"""inheritance"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """made a square class"""
    def __init__(self, size):
        self.integer_validator(size)
        self.size = size
    def area(self):
        return self.size * self.size
