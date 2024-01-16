#!/usr/bin/python3
def islower(c):
    nord = ord(c)
    for i in range(97, 123):
        if nord == i:
            return True
    return False
