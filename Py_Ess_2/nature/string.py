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

print('kappa'.find('a',1,4))
print('kappa'.find('a',2,4))

print("asd123".isalnum())
print("lambda".isalnum())
print("30".isalnum())
print("@".isalnum())
print("lambda_30".isalnum())
print("".isalnum())

print('hello'.isalpha())
print('hi123'.isalpha())
print("2018".isdigit())
print("2018abc".isdigit())

print('hi'.islower())
print('Hi'.islower())

print(' \n '.isspace())
print(" ".isspace())
print("moo moo moo".isspace())

print('hi'.islower())
print('Hi'.islower())
print('HI'.islower())

print('hi'.isupper())
print('Hi'.isupper())
print('HI'.isupper())

print("-".join(["hello", "hi", "greetings"]))
print(",".join(["june","july","august"]))

print("ASDF".lower())
print("["+"   hello   ".lstrip()+"]")

print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

print("www.cisco.com".replace("cisco.com","pythoninstitute.org"))
print("this is it".replace("is", "are"))
print("Apple juice".replace("juice",""))

print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta",9))
print("tau tau tau".rfind("ta",3,9))

print("["+"   hello   ".rstrip()+"]")
print("  ps     cd\nls".split())

print("omega".startswith("me"))
print("omega".startswith("ome"))

print("["+"   hello   ".strip()+"]")

print("i know that i need to learn alot".swapcase())
print("I KNOW THAT I NEED TO LEARN ALOT".swapcase())
print("i know that i need to learn alot".title())
print("I KNOW THAT I NEED TO LEARN ALOT".title())
print("i know that i need to learn alot".upper())
print("I KNOW THAT I NEED TO LEARN ALOT".lower())
print("i know that i need to learn alot".capitalize())
print("I KNOW THAT I NEED TO LEARN ALOT".capitalize())

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

s1 = "where is the snow of yesteryear"
s2 =s1.split()
print(s2)
print(s2[-2])

the_list = ['where', 'is', 'the', 'snow', 'of', 'yesteryear']
s = '*'.join(the_list)
print(s)

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)

# Your own split

def mysplit(strng):
    if strng == '' or strng.isspace():
        return []
    lst = []
    word = ''
    inword = not strng[0].isspace()
    for x in strng:
        if inword:
            if not x.isspace():
                word = word + x
            else:
                lst.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
        lst.append(word)
    return lst
     
print(mysplit("To be or not be, that is the question"))    
print(mysplit("To be or not be,that is the question")) 
print(mysplit(" ")) 
print(mysplit(" abc "))
print(mysplit("")) 


print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabeth')
print('beta' > 'Beta')
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' == '80')
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('20' != 1)
# print('20' > 20)
# print('20' < 20)
print(20 < 20)

greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)

it = 13
fl = 1.3
si = str(it)
sf = str(fl)
print(si + sf)

si = '13'
sf = '1.3'
it = int(si)
fl = float(sf)
print(it + fl)

print('smith' > 'Smith')
print('Smiths' < 'Smith')
print('smith' > '1000')
print('11' < '8')

s1 = "Where are the snow of yesteryear?"
s2 = s1.split()
s3 = sorted(s2)
print(s3[2])

# s1 = '12.8'
# i = int(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)

s1 = '12.8'
i = int(float(s1))     # i = 12
s2 = str(i)            # s2 = '12'
f = float(s2)          # f = 12.0
print(s1 == s2)        # Comparing '12.8' == '12' → False

"""

# Caesar cipher - encrypting a message.
message = input("Enter a message: ")
cipher = ''

for char in message:
    if char.isspace():
        cipher += ' '
    elif char.isalpha():
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')  # Wrap around after 'Z'
        cipher += chr(code)
    else:
        cipher += char  # Optionally keep punctuation

print(cipher)

# Caesar cipher - decrypting a message.
cipher = input("Enter your cryptogram: ")
text = ''
for char in cipher:
    if char.isspace():
        text += ' '
        continue
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')  # Wrap from A to Z
    text += chr(code)
text = text.lower()
print(text)


# Number processor
line = input("Enter a line of numbers - separate them with spaces: ")
string = line.split()
total = 0

try:
    for substr in string:
        total += float(substr)
    print('total = ', total)
except:
    print(substr, "is not a number")


# IBAN Validator
iban = input("Enter IBAN, please: ").replace(' ', '')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 34:
    print("IBAN entered is too long.")
else:
    iban = iban[4:] + iban[:4].upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


# Improving the Caeser Cipher

shift = 0

while shift == 0:
    try:
        shift = int(input("Enter the cipher shift value(1..25):"))
        if shift not in range(1, 26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("incorrect shift value")

cipher = ''

for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        code -= first
        code %= 26
        cipher += chr(first + code)
    else:
        cipher += char


# Palindromes

text = input("Enter a text: ")
if len(text) > 1 and text.upper() == text[::-1].upper():
    print("It's a palindrome")
else:
    print("It's not a palindrome")

"""

palindromes = """
🅰️ Single-Word Palindromes:
madam
racecar
level
deified
civic
radar
rotor
refer
stats
noon

🧾 Palindromic Phrases (ignore spaces/punctuation/case):
nurses run
never odd or even
a man a plan a canal panama
was it a car or a cat I saw
Eva, can I see bees in a cave?
no lemon, no melon
do geese see God
Madam In Eden, I'm Adam
Mr. Owl ate my metal worm
A Santa at NASA

🔢 Palindromic Numbers:
121
1331
12321
88888888
1001
45654
"""
print(palindromes)


"""
# Anagrams

str_1 = input("Enter the first string: ").replace(" ","")
str_2 = input("Enter the second string: ").replace(" ","")
strx_1 = ''.join(sorted(str_1.upper()))
strx_2 = ''.join(sorted(str_2.upper()))
if len(strx_1) > 0 and strx_1 == strx_2:
    print("Anagrams")
else:
    print("Not Anagrams")

"""

anagrams = """
listen silent enlist inlets tinsel
evil live veil vile
angel glean gleaned
dusty study
night thing
brag grab
cinema iceman anemic
save vase
earth heart hater
bored robed
state taste
rescue secure
fired fried
loop pool polo
inch chin
care race acre
stone tones onset
meat team mate
"""
print(anagrams)


