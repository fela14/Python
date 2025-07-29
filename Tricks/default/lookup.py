from string import Template

name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

def greeting(userid):
    x = Template('Hi $userid')
    sub = x.substitute(userid = name_for_userid[userid])
    return sub

print(greeting(382))
# print(greeting(959999))       # KeyError: 959999

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s' % name_for_userid[userid]
    else:
        return 'Hi there'
print(greeting(590))
print(greeting(959999))  

def greeting(userid):
    try: 
        return 'Hi %s' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'
print(greeting(950))
print(greeting(10000)) 
print('*'*25) 

def greeting(userid):
    return f'Hi {name_for_userid.get(userid, 'there')}'

print(greeting(590))
print(greeting(10000)) 

xs = {'a':4, 'c':3, 'b':2.7, 'd':1}
print(sorted(xs.items()))

print(sorted(xs.items(), key=lambda x: x[1]))

from operator import itemgetter

print(sorted(xs.items(), key=itemgetter(1)))
print(sorted(xs.items(), key=lambda x: abs(x[1])))
print(sorted(xs.items(), key = lambda x: x[1], reverse=True))

def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y,
    }.get(operator, lambda: None)()
print(dispatch_dict('mul', 3,8))
print(dispatch_dict('unknown', 3,8))