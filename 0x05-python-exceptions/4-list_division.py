#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for num in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[num] / my_list_2[num]
        except(TypeError, ValueError):
            print("wrong type")
        except(ZeroDivisionError):
            print("division by 0")
        except(IndexError):
            print("out of range")
        finally:
            my_list_3.append(quotient or 0)
    return my_list_3
