my_items = ['a', 'b', 'c']
i = 0
while i < len(my_items):
    print(my_items[i]) 
    i += 1

print(range(len(my_items)))

from string import Template
for item, value in enumerate(my_items):
    print(f'{item}: {value}')

emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com'
}

for name, email in emails.items():
    print(f'{name} -> {email}')

# --- List comprehension ---

squares = [x*x for x in range(10)]
print(squares)

# instead of

squares = []
for x in range(10):
    squares.append(x*x)
print(squares)

even_squares = [x*x for x in range(10) if x%2==0]
print(even_squares)

# instead of 

even_squares = []
for s in range(10):
    if s%2==0:
        even_squares.append(s*s)
print(even_squares)

set_squares = set([x*x for x in range(-9,10)])
print(set_squares)

dict_squares = {x: x*x for x in range(5)}
print(dict_squares)
