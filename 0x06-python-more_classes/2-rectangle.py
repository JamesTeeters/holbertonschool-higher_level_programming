#!/usr/bin/python3
"""
Make a Rectangle
"""

class Rectangle:
    """Created Rectangle Class"""
    def __init__(self, width=0, height=0):
        """set attributes of rectangle"""
        self.__width = width
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width <= 0 or self.__height <= 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height <= 0 or self.__width <= 0:
            return ""
        return (("#" * self.__width + "\n") * (self.__height -1) + ("#" * self.width))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
