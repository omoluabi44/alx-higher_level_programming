#!/usr/bin/python3
""" base """
import json

class Base:
    """
    parent class for  class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ assigne value to id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1,1)

        elif cls.__name__== "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dictionary_list = cls.from_json_string(json_data)
                instances = [cls.create(**dictionary) for dictionary in dictionary_list]
                return instances
        except FileNotFoundError:
            return []
