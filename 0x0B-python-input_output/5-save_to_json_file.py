#!/usr/bin/python3
"""
open and and write an objects to a the using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ print the file content to the stdout """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
