class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
sun = Star('Sun', 'Milky Way')
print(sun)

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy
    
sun = Star('Sun', 'Milky Way')
print(sun)

# issubclass
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end='\t')
    print()

# isinstance
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end='\t')
    print()

# is 
class SampleClass:
    def __init__(self, val):
        self.val = val

obj_1 = SampleClass(0)
obj_2 = SampleClass(2)
obj_3 = obj_1
obj_3.val += 1

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_1)
print(obj_1.val, obj_2.val, obj_3.val)

str_1 = 'Mary had a little '
str_2 = 'Mary had a little lamb'
str_1 += 'lamb'

print(str_1 == str_2, str_1 is str_2)


class Super:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My name is "+ self.name

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")
print(obj)

class Super:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My name is "+ self.name

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")
print(obj)

class Super:
    supVar = 2

class Sub(Super):
    subVar = 1

obj = Sub()
print(obj.subVar)
print(obj.supVar)

class Super:
    def __init__(self):
        self.supVar = 2

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 1

obj = Sub()
print(obj.subVar)
print(obj.supVar)

class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
    
obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1)
print(obj.variable_2, obj.var_2, obj.fun_2)
print(obj.variable_3, obj.var_3, obj.fun_3)

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
    
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
    
class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

class SuperA:
    var = 10
    def fun(self):
        return 11
    
class SuperB:
    var = 20
    def fun(self):
        return 21
    
class Sub(SuperB):
    pass

obj = Sub()
print(obj.var, obj.fun())

class Left:
    var = 'L'
    var_left = 'LL'
    def fun(self):
        return "Left"
    
class Right:
    var = 'R'
    var_right = 'RR'
    def fun(self):
        return "Right"
    
class Sub_1(Left, Right):
    pass

class Sub_2(Right, Left):
    pass
obj_1 = Sub_1()
obj_2 = Sub_2()
print(obj_1.var, obj_1.var_left, obj_1.var_right, obj_1.fun())
print(obj_2.var, obj_2.var_left, obj_2.var_right, obj_2.fun())

class One:
    def do_it(self):
        print("do_it from one")
    
    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from two")

one = One()
two = Two()

one.doanything()
two.doanything()

import time

class TrackedVehicle:
    def control_track(self, left, stop):
        pass

    def turn(self, left):
        self.control_track(left, True)
        time.sleep(0.25)
        self.control_track(left, False)

class WheeledVehicle:
    def turn_front_wheels(self, left, on):
        pass

    def turn(self, left):
        self.turn_front_wheels(left, True)
        time.sleep(0.25)
        self.turn_front_wheels(left, False)

import time

class TrackedVehicle:
    def control_track(self, left, stop):
        # Implement actual control logic here
        print(f"Track {'left' if left else 'right'} {'stopped' if stop else 'started'}")

    def turn(self, left):
        self.control_track(left, True)
        time.sleep(0.25)
        self.control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(self, left, on):
        # Implement actual control logic here
        print(f"Front wheels {'left' if left else 'right'} turned {'on' if on else 'off'}")

    def turn(self, left):
        self.turn_front_wheels(left, True)
        time.sleep(0.25)
        self.turn_front_wheels(left, False)

"""
class Top:
    def m_top(self):
        print("top")
        
class Middle(Top):        
    def m_middle(self):
        print("middle")

class Buttom(Middle):
    def m_buttom(self):
        print("buttom")

object = Buttom()
object.m_buttom()
object.m_middle()
object.m_top()

class Buttom(Middle, Top):
    def m_buttom(self):
        print("buttom")

object = Buttom()
object.m_buttom()
object.m_middle()
object.m_top()

class Buttom(Top, Middle):
    def m_buttom(self):
        print("buttom")

object = Buttom()
object.m_buttom()
object.m_middle()
object.m_top()

# The diamond problem

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()


class Top:
    def m_top(self):
        print('top')

class Middle_Left(Top):
    def m_middle(self):
        print('middle_left')

class Middle_Right(Top):
    def m_middle(self):
        print('middle_right')

class Buttom(Middle_Left, Middle_Right):
    def m_button(self):
        print("buttom")

object = Buttom()
object.m_buttom()
object.m_middle()
object.m_top()
"""

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name
    
class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouse")
print(professor_mouse, Mouse.Population)

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
    def __str__(self):
        return self.breed + "says: Woof!"
    
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"
    
class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mr Intruder"
    
rocky = SheepDog("Collie")
luna = GuardDog("Dobbermann")
print(rocky)
print(luna)
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
print(luna is luna, rocky is luna)
print(rocky.kennel)
