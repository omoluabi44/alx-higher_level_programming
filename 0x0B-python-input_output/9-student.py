#!/usr/bin/python3
""" return dict reprentation of a class attribute """


class Student:
    """ class instantiation """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """ return the dict """
    def to_json(self):
        return self.__dict__
