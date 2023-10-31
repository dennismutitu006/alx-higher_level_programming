#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    print("is negative")
print("Last digit of {} is {} and is ".format(number, d), end="")
if d > 0:
    print("is positive")
elif d == 0:
    print("is zero")
