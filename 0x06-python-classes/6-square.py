#!/usr/bin/python3


""" create  class of square """


class Square:
    """ initialize the size and position """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        """ the getter for size """
    @property
    def size(self):
        return self.__size
    """ the getter for position """
    @property
    def position(self):
        return self.__position
    """size setter """
    @size.setter
    def size(self, value):
        """ getter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """ position setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) !=\
           2 or not all(isinstance(x, int) for x in value)\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """ return the area """
    def area(self):
        return self.__size ** 2
    """ print this """
    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
