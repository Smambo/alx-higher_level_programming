#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = int(str(number)[-1]) * -1
else:
    lastDigit = int(str(number)[-1])
string = "Last digit of"
if lastDigit > 5:
    print(f"{string} {number:d} is {lastDigit:d} and is greater than 5")
elif lastDigit == 0:
    print(f"{string} {number:d} is {lastDigit:d} and is 0")
elif lastDigit < 6:
    print(f"{string} {number:d} is {lastDigit:d} and is less than 6 and not 0")
