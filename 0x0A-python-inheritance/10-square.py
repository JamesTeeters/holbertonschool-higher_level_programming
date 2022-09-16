#!/usr/bin/python3
"""inheritance"""


class BaseGeometry:
    """created empty class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size
    
    def area(self):
        return self.size * self.size
