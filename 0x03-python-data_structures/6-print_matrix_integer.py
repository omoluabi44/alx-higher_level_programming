#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for b in i:
            if b != i[-1]:
                print("{:d}".format(b), end=" ")
            else:
                print("{:d}".format(b), end="")
        print()
