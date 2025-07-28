a = [1,2,3]
b = a
print(a)
print(b)
print(a==b)
print(a is b)
c = list(a)
print(c)
print(a==c)
print(a is c)
b.append(4)
print(a)
c.append(5)
print(a)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
class New_Car(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

my_car = Car('red', 37281)
my_new = New_Car('red', 37281)
print(my_new.color)
print(my_car)
print(my_car.color, my_car.mileage)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f'a {self.color} car'
    
my_car = Car('red', 37281)
print(my_car)
print('{}'.format(my_car))

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return '__str__ for Car'
    def __repr__(self):
        return '__repr__ for Car'
    
ford = Car('white', 5336)
print(ford)
print('{}'.format(ford))
print(str(ford))
print(repr(ford))
print(str([ford]))

import datetime

date = datetime.datetime.today()
print(str(date))
print(repr(date))

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    # def __repr__(self):
    #     return f'Car({self.color!r}, {self.mileage!r})'
    def __repr__(self):
        return f'Car('+ repr(self.color) + ', ' + repr(self.mileage) + ')'
benx = Car('black', 8622)
print(benx)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage})'
    def __str__(self):
        return f'a {self.color} car'

benx = Car('black', 8622)
print(benx)

