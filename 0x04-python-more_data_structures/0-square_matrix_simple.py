#!/usr/bin/python3
list_me = []


def square_matrix_simple(matrix=[]):
    for row in matrix:
        list_me2 = []
        for i in row:
            list_me2.append(i ** 2)
        list_me.append(list_me2)
    return list_me
