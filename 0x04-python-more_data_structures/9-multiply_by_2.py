def multiply_by_2(a_dictionary):
    a_dictionary2 = a_dictionary.copy()
    for i in a_dictionary2:
        new_dic = (f'{i}: {a_dictionary2[i]}')
        a_dictionary2[i] = int((f'{a_dictionary2[i]} ')) * 2
    return (a_dictionary2)
