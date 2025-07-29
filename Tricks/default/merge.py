xs = {'a': 1, 'b':2}
ys = {'b': 3, 'c':4}

zs = {}
zs.update(xs)
zs.update(ys)
print(zs)

dict1 = {'a': 1, 'b':2}
dict2 = {'b': 3, 'c':4}

def update(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value

update(dict1, dict2)
print(dict1)

up = dict(xs, **ys)
print(up)

up_up = {**xs, **ys}
print(up_up)

