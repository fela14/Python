# import math
# import sys
# from math import *
from math import pi, sin
import math, sys

print(math.sin(math.pi/2))
print(math.e)

print(sin(pi/2))
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None
print(sin(pi/2))

#from math import pi, sin
#print(sin(pi/2))

import math as m
print(m.sin(m.pi/2))

from math import pi as PI, sin as sine

print(sine(PI/2))

# Print names on all entities within the math module
for name in dir(math):
    print(name, end="\t")
#dir(math)

from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi/2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

from math import e, exp, log

print(pow(e,1) == exp(log(e)))
print(pow(2,2) == exp(2*log(2)))
print(log(e,e) == exp(0))

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x),  floor(y))     # ceil - smallest integer >= x
print(floor(-x),  floor(-y))   # floor - larget integer <= x
print(ceil(x),  ceil(y))       # trunc - remove the decimal
print(ceil(-x),  ceil(-y)) 
print(trunc(x),  trunc(y)) 
print(trunc(-x),  trunc(-y)) 

from random import random

for i in range(5):
    print(random())
print("*******************")

from random import random, seed

seed(0)
for i in range(5):
    print(random())
print("*******************")

import random
random.seed(10)
print(random.randint(1, 100))

from random import randrange, randint

print(randrange(8), end=' ')
print(randrange(0, 9), end= ' ')
print(randrange(0, 9, 3), end=' ')
print(randint(0,7))

from random import choice, sample

for i in range(10):
    print(randint(1,10))

my_list=[2,3,54,56,3,657,34,4646,86,45]

print(choice(my_list))
print(sample(my_list, 5))
print("*"*10)
print(sample(my_list, 9))

from platform import platform, machine, processor, system, version

print(platform())
print(platform(1))
print(platform(0,1))
print(machine())
print(processor())
print(system())
print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())
for atr in python_version_tuple():
    print(atr)
