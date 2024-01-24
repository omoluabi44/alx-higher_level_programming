#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary)
    for i in sort:
        new_dic =(f'{i}: {a_dictionary[i]}')
        print(new_dic)
