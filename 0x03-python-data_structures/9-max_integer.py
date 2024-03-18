#!/usr/bin/python3

def max_integer(my_list=[]):
    sent = None
    if len(my_list) > 0:
        sent = my_list[0]
        for item in my_list:
            if item > sent:
                sent = item
    return sent
