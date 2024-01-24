#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mul(num):
        return num * number
    new = list(map(mul, my_list))
    return new
