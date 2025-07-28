xs = [[1,2,3], [4,5,6], [7,8,9]]
ys = list(xs)   # make a shallow copy
print(xs)
print(ys)

xs.append(['new sublist'])
print(xs)
print(ys)

import copy
xs = [[1,2,3], [4,5,6], [7,8,9]]
zs = copy.deepcopy(xs)
print(zs)
xs[1][0] = 'X'
print(xs)
print(zs)

xs = [[1,2,3], [4,5,6], [7,8,9]]
bs = copy.copy(xs)
xs[0][0] = 'X'
print(xs)
print(bs)

xs = [[1,2,3], [4,5,6], [7,8,9]]
vs = list(xs)   # make a shallow copy
xs[0][0] = 'V'
print(xs)
print(vs)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'
a = Point(23,42)
b = copy.copy(a)
print(a)
print(b)
print(a is b)

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, {self.bottomright!r})')
    
my_rect = Rectangle(Point(10,20), Point(25,35))
print(my_rect)
your_rect = copy.copy(my_rect)
print(your_rect)
my_rect.topleft.x = 50
your_rect.bottomright.y = 90
print(my_rect)
print(your_rect)
print(my_rect is your_rect)

his_rect = Rectangle(Point(70,20), Point(45,35))
her_rect = copy.deepcopy(his_rect)
print(his_rect)
print(her_rect)
print(his_rect is her_rect)
his_rect.topleft.x = 55
her_rect.bottomright.y = 77
print(his_rect)
print(her_rect)

