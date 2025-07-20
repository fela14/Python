#!/usr/bin/env python3

""" module.py - an example of a python module """

from sys import path
import sys

for p in sys.path:
    print(p)

path.append('..\\modules')


__counter = 0


for p in sys.path:
    print(p)

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prod(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod  *= element
    return prod


if __name__ == '__main__':
    print("I prefer to be a module but i can do some test for you")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prod(my_list) == 120)

