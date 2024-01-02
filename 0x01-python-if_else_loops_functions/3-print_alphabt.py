#!/usr/bin/python3
number = 97
while number >= 97 and number <= 122:
    if number == 101 or number == 113:
        pass
    else:
        print("{:c}".format(number), end="")
    number += 1
