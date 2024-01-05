#!/usr/bin/python3
for i in range(-122, -96):
    if abs(i) % 2 == 0:
        print("{:c}".format(abs(i)), end="")
    else:
        print("{:c}".format(abs(i) - 32), end="")
