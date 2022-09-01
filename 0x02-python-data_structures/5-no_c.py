#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for i in my_list:
        while 'c' in my_list:
            my_list.remove('c')
        while 'C' in my_list:
            my_list.remove('C')
        my_string = ''.join(str(i) for i in my_list)
    return my_string
