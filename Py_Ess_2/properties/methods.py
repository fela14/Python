class Classy:
    def method(self):
        print("method")

obj = Classy()
obj.method()

class Classy:
    def method(self, par):
        print("method: ", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

class Classy:
    varia = 3
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3
obj.method()

class Classy:
    def other(self):
        print('other')

    def method(self):
        print('method')
        self.other()

obj = Classy()
obj.method()

class Classy:
    def __init__(self, value):
        self.var = value
        
obj = Classy('object')
print(obj.var)

class Classy:
    def __init__(self, value = None):
        self.var = value
        
obj_1 = Classy('object')
obj_2 = Classy()
print(obj_1.var)
print(obj_2.var)

class Classy():
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible()
try:
    obj.hidden()
except:
    print('Failed')
obj._Classy__hidden()

class Classy:
    varia = 1 
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

class Classy:
    pass

print(Classy.__name__)
obj = Classy()
# print(obj.__name__)
print(type(obj).__name__)
print(Classy.__module__)
print(obj.__module__)

class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('(', end=' ')

    for x in cls.__bases__:
        print(x.__name__, end = ' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)


class MyClass():
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name. startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val+1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

class Sample:
    def __init__(self):
        self.name = Sample.__name__

    def myself(self):
        print("My name is "+self.name+ "living in a "+ Sample.__module__)

obj = Sample()
obj.myself()

class Snake():
    pass

class Python(Snake):
    pass

print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be', Python.__name__)







