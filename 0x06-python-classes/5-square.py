#!/usr/bin/python3


""" class that define square """


class Square:

    """ iniiatialize the size to self.size"""
    def __init__(self, size=0):
        self.__size = size

    """ the getter """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """ getter """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """ return the area """
    def area(self):
        return self.__size ** 2
    """ print # by multiplying it with size """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
