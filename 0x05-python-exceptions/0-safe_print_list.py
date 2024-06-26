#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            list_num += 1
        except IndexError:
            continue
    print("")
    return list_num
