#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    New_list = []
    for i in my_list:
        if i % 2 == 0:
            New_list.append(True)
        else:
            New_list.append(False)
    return New_list
