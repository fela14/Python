word='by'
print(len(word))

empty=''
print(len(empty))

i_am = 'I\'m'
print(len(i_am))

multiline= """
This is python
Monty Python
"""
print(len(multiline))

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5*'a')
print('b'*4)

char_1 = 'a'
char_2 = ' '

print(ord(char_1))
print(ord(char_2))
print(chr(97))
print(chr(945))

# chr(ord(x)) == x
# ord(chr(x)) == x

the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

for character in the_string:
    print(character)

alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

alphabeth = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabeth)
print("F" in alphabeth)
print("l" in alphabeth)
print("ghi" in alphabeth)
print("Xyz" in alphabeth)
print("abc" in alphabeth)

print("f" not in alphabeth)
print("F" not in alphabeth)
print("l" not in alphabeth)
print("ghi" not in alphabeth)
print("Xyz" not in alphabeth)
print("abc" not in alphabeth)

# del alphabeth[0] # wont work 
# alphabeth.append('A')
# alphabeth.insert(5,'Q')
print(alphabeth)

alphabeth = "bcdefghijklmnopqrstuvwxy"

alphabeth = 'a' + alphabeth
alphabeth = (alphabeth + 'z')
print(alphabeth)

print(min('hdfTgvj'))
t = 'The Knights Who Say "Ni!"'
print ('['+min(t)+']')
print ('['+max(t)+']')
t = [0,1,2]
print(min(t))
print(max(t))

t = "aAbByYzZA"
print(t.index("b"))
print(t.index("Z"))
print(t.index("A"))
print(t.count('b'))
print(t.count('A'))

print(list("abcabc"))

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

s = "yesteryears"
the_list = list(s)
print(the_list[3:6])

for ch in "abc":
    print(chr(ord(ch)+1), end="")
print()

print('aBcD'.capitalize())
print('ALPHA'.capitalize())
print('Alpha'.capitalize())
print('123'.capitalize())

print('['+ 'abc'.center(10) + ']')
print('['+ 'Beta'.center(2) + ']')
print('['+ 'Beta'.center(4) + ']')
print('['+ 'Beta'.center(6) + ']')

print('['+ 'gamma'.center(12, '+') + ']')

if 'epsilon'.endswith('on'):
    print("yes")
else:
    print("no")

t = "dyugjewk"
print(t.endswith("ewk"))
print(t.endswith("ewdaak"))
print(t.endswith("aedf"))

t="theta"
print(t.find("eta"))
print(t.find("etewa"))
print(t.find("e53ta"))

text = """
Learning to code is both challenging and rewarding, 
offering a gateway to creativity, problem-solving, 
and career opportunities in today’s digital world. 
It teaches persistence, logical thinking, and 
attention to detail, all while empowering you to 
build tools, automate tasks, or even create entire 
applications from scratch. As you progress, small
victories—like solving a bug or completing a 
project—become incredibly satisfying. The journey
may seem overwhelming at first, but consistent 
practice and curiosity go a long way. Whether 
you're writing Python scripts or designing web
pages, every line of code written adds to your
skills and confidence as a developer.
"""

fnd = text.find("the")
while fnd != -1:
    print(fnd)
    fnd = text.find("the", fnd+1)

