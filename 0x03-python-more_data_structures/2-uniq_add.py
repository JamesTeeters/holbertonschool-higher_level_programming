#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    num = set(my_list)
    for i in num:
        total += i
    return total
