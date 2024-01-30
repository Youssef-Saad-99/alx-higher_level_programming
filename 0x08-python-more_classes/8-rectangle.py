#!/usr/bin/python3
"""
    Defining the rectangle class
"""


class Rectangle:
    """representation of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns printable string representation of the rectangle"""
        if not self.__height or not self.__width:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                 self.height) [:-1]

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.height)

    def __del__(self):
        """print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger of two rectangles.
        
        Args:
            rect_1: the first rectangle.
            rect_2: the second rectangle.
        Raises:
            TypeError: if rect_1, rect_2 are not instances of rectangle.
        Returns:
            The bigger area of rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
