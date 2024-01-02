#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > 10 else number % -10
print(f"Last digit of {number:d} is {last:d} and is ", end = "")
if mod > 5:
    print("greater than 5")
elif mod == 0:
    print("0")
else:
    print("less than 6 and not 0")
