x = list(map(lambda x: x + 2, [1,2,3,4]))
print(x)

add = lambda x, y: x + y
print(add(3,5))

# More verbose
def add(x, y):
    return x + y
print(add(3,5))

result = (lambda x, y: x + y)(10, 10)
print(result)

tuples = [(1,'hello'), (16, 'hi'), (9, 'hey'), (14, 'holla')]
x = sorted(tuples, key = lambda x: x[1])
print(x)

# Without lamdba
def get_second(item):
    return item[1]

tuples = [(1,'hello'), (16, 'hi'), (9, 'hey'), (14, 'holla')]
x = sorted(tuples, key = get_second, reverse=True)
print(x)

# Harmful
x = list(filter(lambda x: x%2==0, range(20)))
print(x)

# Better
x = [x for x in range(20) if x % 2 == 0]
print(x)


