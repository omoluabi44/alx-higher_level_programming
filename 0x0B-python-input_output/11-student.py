#!/usr/bin/python3
""" return dict reprentation of a class attribute """


class Student:
    """ class instantiation """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """ return the dict """
    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if isinstance(attrs, list) and \
           all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for key, value in json.items():
            setattr(self, key, value)
