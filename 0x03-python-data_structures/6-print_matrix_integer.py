#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for num in element:
            print("{:d}".format(num), end="")
            if num != element[len(element)-1]:
                print(" ", end="")
        print()
