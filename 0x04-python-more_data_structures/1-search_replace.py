#!/usr/bin/python3
new_list = []


def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return (new_list)
