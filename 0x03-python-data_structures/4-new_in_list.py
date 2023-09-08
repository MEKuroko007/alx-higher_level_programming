#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    tmp=my_list[:]
    if idx >= 0 and idx < len(my_list):
        tmp[idx] = element
        return tmp
    return my_list