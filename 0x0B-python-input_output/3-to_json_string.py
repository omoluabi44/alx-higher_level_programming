#!/usr/bin/python3
"""
serielized object
"""


def to_json_string(my_obj):
    import json
    """ serialize """
    return json.dumps(my_obj)
