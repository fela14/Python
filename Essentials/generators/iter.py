
class Fib:
    def __init__(self, n):
        print("__init__")
        self.__n = n
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self
    
    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)

class Fib():
    def __init__(self, n):
        print("__init__")
        self.__n = n
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self
    
    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
    
class Class():
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class_iter")
        return self.__iter
    
object = Class(8)
for i in object:
    print(i)

# The yield statement
def fun(n):
    for i in range(n):
        return i
print(fun(9))

def fun(n):
    for i in range(n):
        yield i
for val in fun(5):
    print(val)

def power_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
for val in power_of_2(8):
    print(val, end=' ')
print()

def power_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
x = [val for val in power_of_2(8)]
print(x)

def power_of_2(n):
    power = 1
    for x in range(n):
        yield power
        power *= 2
t = list(power_of_2(8))
print(t)

def power_of_2(n):
    power = 1
    for x in range(n):
        yield power
        power *= 2
for i in range(20):
    if i in power_of_2(20):
        print(i)

# The fibonacci number generator

def fib(n):
    p = pp = 1
    for i in range(n):
        if x in [0,1]:
            yield 1
        else:
            ret = p + pp
            p, pp = pp, ret
            yield ret
a = list(fib(8))
print(a)

# More about list comprehensions
list_1 = []
for x in range(6):
    list_1.append(10 ** x)

list_2 = [(10 ** x) for x in range(6)]

print(list_1)
print(list_2)

the_list = []
for x in range(6):
    the_list.append(1 if x%2==0 else 0)
print(the_list)

the_list = [1 if x%2==0 else 0 for x in range(6)]
print(the_list)

# List comprehensions vs generators

the_list = [1 if x%2 == 0 else 0 for x in range(10)]
the_generator = (1 if x%2 == 0 else 0 for x in range(10))

for x in the_list:
    print(x, end='')
for x in the_generator:
    print(x, end='')
print()
for x in [1 if x%2==0 else 0 for x in range(20)]:  #list
    print(x, end=' ')
print()
for x in (1 if x%2==0 else 0 for x in range(20)):  #generator
    print(x, end=' ')
print()

# Lambda

two = lambda: 2
sqr = lambda x: x**2
pwr = lambda x, y: x**y

for i in range(-2, 3):
    print(sqr(i), end = ' ')
    print(pwr(i, two()))

def function(args, fun):
    for x in args:
        print("f(", x, ")=", fun(x), sep ='')

def poly(x):
    return 2*x**2 - 4*x + 2
function([x for x in range(-2, 3)], poly)

def function(args, fun):
    for x in args:
        print("f(",x,")=",fun(x),sep='')
print(function([x for x in range(-2,3)], lambda x: 2*x**2-4*x+2))

# Lambdas and map() function

# map(function, list)

list_1 = [x for x in range(6)]
list_2 = list(map(lambda x: 2**x, list_1))
print(list_1)
print(list_2)
for x in map(lambda x: x**2, list_2):
    print(x, end=' ')
print()

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(6)]
filtered = list(filter(lambda x: x>0 and x%2==0, data))
print(data)
print(filtered)

def outer(par):
    loc=par
var=1
outer(var)
# print(par)
# print(loc)

def outer(par):
    loc=par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())

def make_closure(par):
    loc = par

    def power(p):
        return p**loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(1, fsqr(i), fcub(i))

def foo(x, f):
    return f(x)
print(foo(9, lambda x: x-2))

short_list = ['monty', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda x: x.title(), short_list))
print(new_list)

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

def tag(tg):
    tg2 = tg[0] + "/" + tg[1:]
    def inner(str):
        return tg + str + tg2
    return inner
btag1 = tag("<b>")
print(btag1("Monty Python"))
btag2 = tag("<p>")
print(btag2("Monty Python"))


class Vowels():
    def __init__(self):
        self.vow = 'aeiou'
        self.pos = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos-1]

vowels = Vowels()
for v in vowels:
    print(v, end='')
    
any_list = [1,2,3,4]
even_list = list(map(lambda x: x|1, any_list))
print(even_list)

def rep(replacement="*"):
    def new_rep(text):
        return text.replace(' ', replacement)
    return new_rep
stars = rep()
print(stars("This is my simple replacement"))











