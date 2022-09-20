#!/usr/bin/python3
import random
from sys import exit
number = random.randint(-10000, 10000)
if number > 0:
    new_num = number % 10
elif number < 0:
    new_num = (number % 10) - 10
else:
    new_num = number
while (new_num > 10):
    new_num = new_num % 10
if (number < 0):
    print(f"Last digit of {number} is {new_num} and is less than 6 and not 0")
elif (new_num > 5):
    print(f"Last digit of {number} is {new_num} and is greater than 5")
elif (new_num < 6 and new_num != 0):
    print(f"Last digit of {number} is {new_num} and is less than 6 and not 0")
elif (new_num == 0):
    print(f"Last digit of {number} is {new_num} and is 0")
