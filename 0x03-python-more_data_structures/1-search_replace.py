#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cp = my_list.copy()
    for i in range(len(list_cp)):
        if list_cp[i] == search:
            list_cp[i] = replace
        return list_cp