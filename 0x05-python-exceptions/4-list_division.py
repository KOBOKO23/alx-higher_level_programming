#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_num = 0
    i = 0
    space_new_list = []
    for i in range(list_length):
        try:
            var = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            var = 0
        except ZeroDivisionError:
            print("division by 0")
            var = 0
        except IndexError:
            print("out of range")
            var = 0
        finally:
            space_new_list.append(var)
    return space_new_list
