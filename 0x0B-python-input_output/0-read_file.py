#!/usr/bin/python3
"""
open a file, read and print to the stdout
"""


def read_file(filename=""):
    """ print the file content to the stdout """
    with open(filename, "r", encoding="utf-8") as f:
        read_me = f.read()
        print(read_me)
