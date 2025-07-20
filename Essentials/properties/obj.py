class ExampleClass:
    def __init__(self, val=1):
        self.first = val
    
    def set_second(self, val):
        self.second  = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


class ExampleClass():
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass()

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print(example_object_1._ExampleClass__first)
print(example_object_2._ExampleClass__first)
print(example_object_3._ExampleClass__first)

class ExampleClass:
    counter = 0
    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

class ExampleClass:
    __counter = 0
    def __init__(self, val=1):
        self.__first = val
        ExampleClass.__counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

class ExampleClass:
    varia = 1
    def __init__(self, val):
        #self.varia = val
        ExampleClass.varia = val

print(ExampleClass.__dict__)
example_object = ExampleClass(2)
print(ExampleClass.__dict__)
print(example_object.__dict__)

class ExampleClass():
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b)

try:
    print(example_object.b)
except AttributeError:
    pass

print(example_object.a)
if hasattr(example_object, 'b'):
    print(example_object.b)

class ExampleClass:
    attr = 4

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

class ExampleClass:
    a = 10
    def __init__(self):
        self.b = 20

example_object = ExampleClass()

print(hasattr(example_object, 'a'))
print(hasattr(example_object, 'b'))
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))



