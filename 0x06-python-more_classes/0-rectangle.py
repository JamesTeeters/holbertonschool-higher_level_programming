#!/usr/bin/python3
"""
Make a Rectangle
"""


class Rectangle:
    """Created Rectangle Class"""
    def __init__(self, width=0, height=0):
        """set attributes of rectangle"""
        self.__width = width
        self.__height = height
       

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) != int:
            raise TypeError("Height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")