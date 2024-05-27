#!/usr/bin/python3
'''module for read text file'''


def read_file(filename=""):
    '''Reads a UTF-8 text file and displays it on the screen'''

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
