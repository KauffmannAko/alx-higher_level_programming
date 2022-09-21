#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
"""
last_digit: Returns the last digit of signed number

"""


def last_digit(signed_number):
    digit = abs(number) % 10
    if signed_number < 0:
        return -digit
    if signed_number > 0:
        return digit


last = last_digit(number)
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and not 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
