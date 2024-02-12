#!/usr/bin/python3
'''Module for Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width of this rectangle'''
        return self.__width

    @width.setter
    def width(self, new_value):
        if type(new_value) != int:
            raise TypeError("width must be an integer")
        elif new_value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = new_value

    @property
    def height(self):
        '''height of this rectangle'''
        return self.__height

    @height.setter
    def height(self, new_value):
        if type(new_value) != int:
            raise TypeError("height must be an integer")
        elif new_value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = new_value

    @property
    def x(self):
        '''x of this rectangle'''
        return self.__x

    @x.setter
    def x(self, new_value):
        if type(new_value) != int:
            raise TypeError("x must be an integer")
        elif new_value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = new_value

    @property
    def y(self):
        '''y of this rectangle'''
        return self.__y

    @y.setter
    def y(self, new_value):
        if type(new_value) != int:
            raise TypeError("width must be an integer")
        elif new_value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = new_value

    def area(self):
        '''Calculating the area of this rectangle'''
        return self.__height * self.__width

    def display(self):
        '''display the stdout the Rectangle'''
        new_line = "\n" * self.__y
        print(new_line, end="")
        for i in range(self.__height):
            space = " " * self.__x
            print(space, end="")
            for j in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        '''returns string info about this rectangle'''
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"x": self.__x, "y": self.__y,
                "id": self.__id, "height": self.__height,
                "width": self.__width}
