#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 2:
        while len1 < 2:
            tuple_a += (0,)
            len1 += 1
    if len2 < 2:
        while len2 < 2:
            tuple_b += (0,)
            len 2 += 1
    tuple_c = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] = tuple_b[1]))
    return tuple_c
