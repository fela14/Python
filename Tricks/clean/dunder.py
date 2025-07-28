class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print(t.foo)
print(t._bar)

from module import *
print(external_func())
# print(_internal_func())    # _internal_func' is not defined.
print(_internal_func())      # unless included in __all__ list in module

from module import _secret_func   # would print when specifically
print(_secret_func())             # importing private funcs


# def make_object(name, class):   # SyntaxError: invalid syntax
#     pass

def make_object(name, class_):
    obj = class_(name)
    print(f"Created: {obj}")
    return obj

class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"

make_object('Alice', Animal)
person = make_object('Bob', Person)


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

t = Test()
print(dir(t))

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
# print(t2.__baz)    # ExtendedTest' object has no attribute '__baz'
print(dir(t2))
print(t2._ExtendedTest__baz)
print(t._Test__baz)

class ManglingTest:
    def __init__(self):
        self.__mangled = 'mangled'
        self.hello = 'hello'

    def get_mangled(self):
        return self.__mangled
    
    def get_hello(self):
        return self.hello
    
mang = ManglingTest()
print(mang.get_mangled())
print(mang.get_hello())
print(mang.hello)
# print(mang.__mangled)    # AttributeError: 'ManglingTest' object has no attribute '__mangled'

class MangledMethod:
    def __method(self):
        return 42
    def call_it(self):
        return self.__method()
    
mang = MangledMethod()
print(mang.call_it())
# print(mang.__method())
print(dir(mang))

_MangledGlobal__mangled = 23

class MangledGlobal:
    def call(self):
        return _MangledGlobal__mangled
print(MangledGlobal().call())

class __Myclass:
    def __test(self):
        return "shhh"
my_class = __Myclass()
print(dir(my_class))
print(my_class._Myclass__test())


class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42
print(PrefixPostfixTest().__bam__)


for _ in range(3):
    print('Hello world')

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color)
print(_)
print(mileage)
    
print(2+3)
print(_)

list()
print(list())
_.append(1)
_.append(2)
_.append(3)
print(list())