def print_vector(x,y,z):
    print('<%s,%s,%s>' % (x,y,z))
print_vector(1,0,1)

tuple_vector = (1,2,3)
list_vector = [7,8,9]

print_vector(tuple_vector[0],
             tuple_vector[1],
             tuple_vector[2])
print_vector(*tuple_vector)
print_vector(*list_vector)

genexp = (x*x for x in range(3))
dict_vector = {'x': 10, 'y': 20, 'z': 30}

print_vector(*genexp)
print_vector(**dict_vector)

def foo1(value):
    if value:
        return value
    else:
        return None
def foo2(value):
    if value:
        """ Bare return statement implies `return None` """
        return value
    else:
        return
def foo3(value):
    if value:
        """ Missing return statement implies `return None` """
        return value

print(foo1(0))
print(foo2(0))
print(foo3(0))