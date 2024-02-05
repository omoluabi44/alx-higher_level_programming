#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            x = int(my_list[i])
            print("{:d}".format(x), end="")
            c += 1
        except (TypeError,ValueError):
            pass
    print()
    return c
