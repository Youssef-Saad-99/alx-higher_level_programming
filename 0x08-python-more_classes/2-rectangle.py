#!/usr/bin/python3
"""
    Defining the rectangle class
"""


class Rectangle:
    """representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the private inastance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private inastance attribute width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """getter for the private inastance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private inastance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """get the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
