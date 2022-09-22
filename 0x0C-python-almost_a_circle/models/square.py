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
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__heigth = value

    def update(self, *args, **kwargs):
        """assign arguments to attributes"""
        attr = ['id', 'size', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, attr[i], args[i])
                i += 1
        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])
