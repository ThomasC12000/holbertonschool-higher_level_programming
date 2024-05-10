#!/usr/bin/python3
for LastDigit in range(0, 90):
    if LastDigit / 10 < LastDigit % 10:
        if LastDigit < 89:
            print("{:02d}".format(LastDigit), end=", ")
        else:
            print("{:02d}".format(LastDigit))
