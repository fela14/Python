"""
import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("The operation cannot be done")

print("THE END")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("The operation cannot be done")

print("THE END")

try:
    print("1")
    x = 1/0
    print("2")
except:
    print("Oh dear, something went wrong")
print("3")

try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot devide by zero, sorry")
except ValueError:
    print("You must enter an integer value")
except:
    print("Oh dear, something went wrong.")
print("THE END")

"""

try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("we're done")

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexError:
    print("index")
except:
    print("some")

try:
    y = 1/0
except ZeroDivisionError:
    print("Zero division")
except ArithmeticError:
    print("Arithmetic problem!")
print("THE END")

def bad_fun(n):
    return 1/n
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print("THE END")

def bad_fun(n):
    raise ZeroDivisionError
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END")

def bad_fun(n):
    try:
        return n/0
    except:
        print("I did it again")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("I see")
print("THE END.")

"""
# Assert instruction in action
import math
x= float(input("Enter a number: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)
"""

try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

def foo(x):
    assert x
    return 1/x
try:
    foo(0)
except ZeroDivisionError:
    print("zero")
except:
    print("some")

"""
# AssertionError

from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))
# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
"""

# IndexError

# The code shows an extravagant way of leaving the loop
the_list = [1,2,3,4,5]
do_it = True
ix = 0
while do_it:
    try: 
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
print('Done')

# KeyboardInterrupt

# from time import sleep
# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds +=1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")

# Memory Error

# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

# string = 'x'
# while True:
#     try:
#         string = string + string
#         print(len(string))
#     except MemoryError:
#         print("Don't do that!")

# OverflowError

# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
from math import exp
ex = 1
try: 
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print("This number is too big")

"""
# ImportError

try:
    import math
    import time
    import abracadabra
except:
    print('One of your imports has failed')
"""

# KeyError

dictionary = {'a':'b', 'b':'c', 'c':'d'}
ch = 'a'
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print("No such key as: ", ch)

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = min <= value <= max
            if not ok:
                print("Error: the value is not within the permitted range (" + str(min) + ".." + str(max) + ")")
        except ValueError:
            print("Error: wrong input")
    return value

# Call the function
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("You entered:", v)





