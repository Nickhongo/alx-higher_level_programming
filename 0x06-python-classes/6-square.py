#!/usr/bin/python3
"""Module contains a class that defines a square"""

class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes instance attributes for instances of a square

        Args:
            size: length of the square
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """defines size of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        """defines lenght of a square
        Args:
            value: values representing sizes of the square
        """
        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """defines position of the square"""
        return self.__position
    @position.setter

    def position(self, value):
        """defines position of the square
        Args:
            value: values of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """defines area of a square"""

    def area(self):
        return self.__size ** 2
    """defines a printing function"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
