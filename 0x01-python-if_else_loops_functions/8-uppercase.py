#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print()