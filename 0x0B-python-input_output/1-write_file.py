#!/usr/bin/python3
"""
open a file, read and print to the stdout
"""


def write_file(filename="", text=""):
    """ print the file content to the stdout """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
