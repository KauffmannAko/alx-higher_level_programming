#!/usr/bin/python3

for i in range(0, 9):
    for num in range(i+1, 10):
        if i == 8:
            print("{0:d}{1:d}".format(i, num))
            break
        print("{0:d}{1:d}".format(i, num), end=", ")
