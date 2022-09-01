#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        case = [True if i % 2 == 0 else False for i in my_list]
        return case
    else:
        return None
