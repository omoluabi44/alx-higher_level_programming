#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    for i in my_list:
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        elif idx == i:
            del my_list[idx]
    return my_list
