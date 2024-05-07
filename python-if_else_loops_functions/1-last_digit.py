#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = abs(number) % 10
if number < 0:
    LastDigit *= -1
if LastDigit > 5:
    print(f'Last digit of {number} is {LastDigit} and is greater than 5')
elif LastDigit == 0:
    print(f'Last digit of {number} is {LastDigit} and is 0')
elif LastDigit < 6:
    print(f'Last digit of {number} is {LastDigit} and is less \
than 6 and not 0')
