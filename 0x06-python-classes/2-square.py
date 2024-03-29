#!/usr/bin/python3


""" class that define square """


class Square:

    """ create the class"""
    def __init__(self, size=0):

        """ initialize the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
