#!/usr/bin/python3
"""
serielized object
"""
import json


def to_json_string(my_obj):
    """ serialize """
    return json.dumps(my_obj)
