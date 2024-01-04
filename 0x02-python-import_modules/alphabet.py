#!/usr/bin/python3
def alpha():
    for i in range(65, 91):
        print("{:c}".format(i), end="\n" if i == 90 else "")
