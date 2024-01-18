#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys.argv[0] = "argument"
    n = len(sys.argv)
    b = len(sys.argv) - 1

    if b == 0:
        print("{} {}s.".format(b, sys.argv[0]))
    elif b == 1:
        print("{} {}:".format(b, sys.argv[0]))
    else:
        print("{} {}s:".format(b, sys.argv[0]))
    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
