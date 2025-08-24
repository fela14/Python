def integer():
    for i in range(1,9):
        yield i
chain = list(integer())
print(chain)

def squared(seq):
    for i in seq:
        yield i*i

chain = squared(integer())
print(list(chain))

def negative(seq):
    for i in seq:
        yield -i

ch = negative(squared(integer()))
print(list(ch))

# even better

integers = range(1,9)
squares = [i*i for i in integers]
neg = [-x for x in squares]
print(neg)


