#!/usr/bin/python3
"""
this module defines a python class-to-json function """


def class_to_json(obj):
    """ return the dict repr. if of a simple data struc."""
    return obj.__dict__
