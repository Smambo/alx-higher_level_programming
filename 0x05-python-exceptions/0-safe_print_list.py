#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    if my_list:
        for num in range(x):
            try:
                print("{}".format(my_list[num]), end='')
                elements += 1
            except IndexError:
                print()
                return elements
    print()
    return elements
