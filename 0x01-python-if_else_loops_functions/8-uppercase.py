#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{:c}".format(ord(i)-32), end="\n" if i == str[-1] else "")
        else:
            print("{:s}".format(i))
