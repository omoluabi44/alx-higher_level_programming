#!/usr/bin/python3
"""

this module contain function that add two number

"""


def add_integer(a, b=98):
    """Return the integer addition of a and b

    Args:
    a: first number
    b: second number

    Return:
    the addition of a and b

    Raises:
    TypeError if a or b is not a numbe

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
