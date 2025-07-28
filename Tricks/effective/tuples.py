tup = ('hello', object(), 42)
print(tup)
print(tup[2])
# tup[2] = 23    # TypeError: 'tuple' object does not support item assignment

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
print('color mileage'.split())
car = Car
print(car)

my_car = Car('red', 633.13)
print(my_car.color)
print(my_car.mileage)
print(my_car[0])
print(tuple(my_car))
print(*my_car)
print(my_car) 

Bus = namedtuple('Bus', 'size color')
print('size color'.split())
bus = Bus('big', 'red')
print(*bus)
print(bus)

Car = namedtuple('Car', 'color mileage')

class MyCarWithMethod(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'
my_car = MyCarWithMethod('red', 3663)
print(my_car.hexcolor())

ElectricCar = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

e_car = ElectricCar('red', 7373, 383.3)
print(e_car)

print(e_car._asdict())
print(type(e_car._asdict()))

import json
print(json.dumps(e_car._asdict()))
print(type(json.dumps(e_car._asdict())))

e_car = e_car._replace(color='blue')
print(e_car)

your_car = ElectricCar._make(['brown', 33, 33])
print(your_car)
