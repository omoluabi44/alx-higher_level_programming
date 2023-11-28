#!/usr/bin/python3
def uppercase(str):
    is_upper = ""
    for i in (str):
        convert_digit = ord(i)
        if convert_digit > 96 and convert_digit < 123:
            is_upper = is_upper + chr(convert_digit - 32)
        elif i.isdigit():
            is_upper = is_upper + i
        elif i == " ":
            is_upper += " "
        else:
            is_upper = is_upper + chr(convert_digit)
    print("{}".format(is_upper))
