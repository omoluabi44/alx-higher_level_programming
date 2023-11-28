def uppercase(str):
    is_upper = ""
    for i in (str):
        convert_digit = ord(i)
        if convert_digit > 96 and convert_digit < 123:
            is_upper = is_upper +  chr(convert_digit - 32)
        elif int(i)>= 0 and int(i) <= 99:
            is_upper = is_upper + i
    print(is_upper, end="")
