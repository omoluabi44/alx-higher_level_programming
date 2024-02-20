#!/usr/bin/python3
"""pascal triangle """


def pascal_triangle(n):
    """pascal triangle """
    list2 = []
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(list2[i-1][j-1] + list2[i-1][j])
        list2.append(tmp)
    return list2
