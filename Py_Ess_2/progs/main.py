from sys import path
import modules.module as module
from modules.module import suml, prod

path.append("..\\modules")
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prod(ones))
print(module.__counter)