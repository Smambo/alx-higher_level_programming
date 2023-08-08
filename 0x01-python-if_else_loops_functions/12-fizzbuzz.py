#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        print("{}".format(result) or "{}".format(num), end='')
        print(" ", end='')
