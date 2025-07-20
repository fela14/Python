def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Division failes")
        return None
    else:
        print("Everything is fine")
        return n
    
print(reciprocal(2))
print(reciprocal(0))

def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everthing is fine")
    finally:
        print("It's time to say goodbye")

print(reciprocal(2))
print(reciprocal(0))

try:
    i = int("Hello")
except Exception as e:
    print(e)
    print(e.__str__())

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end=" ")
    if nest > 0:
        print("   +---", end=" ")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)

class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        print("some worse news")
    else:
        print("some bad news")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

# Pizza and Cheese

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

class PizzaError(Exception):
    def __init__(self, message='', pizza='unknown'):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, message='', pizza='unknown', cheese='>110'):
        PizzaError.__init__(self, message, pizza)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 110:
        raise TooMuchCheeseError
    print("Pizza Ready")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza) 

try:
    assert __name__ == '__main__'
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

import math

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

for i in range(5):
    print(i)
