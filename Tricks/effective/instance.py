class Dog:
    num_legs = 4  # <- Class variable
    def __init__(self, name):
        self.name=name  # <- Instance variable

Jack = Dog('Jack')
Jill = Dog('Jill')
print(Jack.name, Jill.name)
print(Jack.num_legs)
print(Jill.num_legs)
print(Dog.num_legs)

Dog.num_legs = 6
print(Dog.num_legs)
print(Jack.num_legs)
print(Jill.num_legs)

Jack.num_legs = 110
print(Jack.num_legs)
print(Jill.num_legs)
print(Jack.__class__.num_legs)

class CountedObject:
    num_instances = 20
    def __init__(self):
        self.__class__.num_instances += 1
print(CountedObject.num_instances)
May = CountedObject()
print(May.num_instances)
June = CountedObject()
print(June.num_instances)
print(CountedObject.num_instances)

class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'instance method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'  
    
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"
pizza = Pizza(['cheese', 'tomatoes'])
print(pizza)

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    
print(Pizza.margherita())
print(Pizza.prosciutto())

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.radius!r}, {self.ingredients!r})'
    
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(radius):
        return 2*radius*math.pi
    
p = Pizza(10, ['tomatoes', 'cheese'])
print(p)
print(p.area())
print(Pizza.circle_area(10))




