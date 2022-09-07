#!/usr/bin/python3
"""added method area"""
class Square:
    """Created class Square"""
    def __init__(self, size=0):
        """Assign atrributes to Square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Assign methods to Square"""
         return self.__size * self.__size