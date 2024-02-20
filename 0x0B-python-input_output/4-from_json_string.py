#!/usr/bin/python3
"""
serielized object
"""
import json


def from_json_string(my_obj):
    """ serialize """
    return json.loads(my_obj)
