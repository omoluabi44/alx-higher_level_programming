#!/usr/bin/python3
"""
open a file, and append
"""


def append_write(filename="", text=""):
    """ append to a file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
