#!/usr/bin/python3
"""Square module"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Constructor.
        Args:
            size: length of a side of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size
    @property
    def size(self):
        """property for the length of a side of this square.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of this square.
        Returns:
            The size square.
        """
        return self.__size ** 2
