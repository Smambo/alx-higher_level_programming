#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    if my_list:
        for num in range(x):
            try:
                print("{:d}".format(my_list[num]), end='')
                elements += 1
            except(TypeError, ValueError):
                pass
    print()
    return elements
