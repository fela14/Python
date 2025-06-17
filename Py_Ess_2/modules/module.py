print("i like to be a module.")
print(__name__) # prints (__main__)
# counter = 0

if (__name__) == "__main__":
    print("i prefer to be a module")
else:
    print("i like to be a module")


__counter = 0

def suml(the_list):
    global __counter
    __counter+=1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __counter
    __counter+=1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if (__name__) == "__main__":
    print("i prefer to be a module but i can do some tests for you.")
my_list=[i+1 for i in range(5)]
print(suml(my_list) == 15)
print(prodl(my_list) == 120)

import sys
for x in sys.path:
    print(x)






