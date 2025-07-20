from os import strerror

try:
    stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt")
    counter = 0
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nChanracters in file =", counter)
except Exception as exc:
    print("Unknown", strerror(exc.errno))


try:
    counter = 0
    stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nNumber of characters:", counter)
except Exception as e:
    print("Unknown", strerror(e.errno))
print()
print("*"*50)

# readline()

try:
    line_counter = char_counter = 0
    stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt")
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            char_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nNumber of lines:", line_counter)
    print("Number of characters:", char_counter)
except Exception as exc:
    print("I/O Error:", strerror(exc.errno))

# readlines()

stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

try:
    lcnt = ccnt = 0
    stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt")
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for char in line:
                ccnt += 1
                print(char, end='')
        lines = stream.readlines(20)
    stream.close()
    print("\n\nNumber of lines:", lcnt)
    print("Number of characters:", ccnt)
except Exception as exc:
    print("I/O Error:", strerror(exc.errno))

try:
    ccnt = lcnt = 0
    for line in open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/file.txt", "rt"):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nNumber of lines:", lcnt)
    print("Number of characters:", ccnt)
except Exception as exc:
    print("I/O Error:", strerror(exc.errno))

try:
    file =open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/new_file.txt", "wt")
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except Exception as exc:
    print("I/O Error:", strerror(exc.errno))            

try:
    file = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/newfile.txt", "wt")
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except Exception as exc:
    print("I/O Error:", strerror(exc.errno)) 

# bytearray

data = bytearray(10)
for i in range (len(data)):
    data[i] = 10 - i
for b in data:
    print(hex(b))

data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i
try:
    file = open("c:/users/Opeyemi/fela_Python/Py_Ess_2/files/file.bin", "wb")
    file.write(data)
    file.close()
except Exception as exc:
    print("I/O Error:", strerror(exc.errno)) 

data = bytearray(10)

try:
    binary_file = open("c:/users/Opeyemi/fela_Python/Py_Ess_2/files/file.bin", "rb")
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except Exception as exc:
    print("I/O Error:", strerror(exc.errno)) 

try:
    binary_file = open("c:/users/Opeyemi/fela_Python/Py_Ess_2/files/file.bin", "rb")
    data = bytearray(binary_file.read()) 
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except Exception as exc:
    print("I/O Error:", strerror(exc.errno)) 

print()

# Recommended to specify the desired number of bytes to read from a file

try:
    binary_file = open("c:/users/Opeyemi/fela_Python/Py_Ess_2/files/file.bin", "rb")
    data = bytearray(binary_file.read(5)) 
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except Exception as exc:
    print("I/O Error:", strerror(exc.errno)) 

print()
print()
print("*"*50)
print()

# Copying giles - a simple and functional tool

from os import strerror
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file:", strerror(e.errno))
    exit(e.errno)
destname = input("Enter the destibation file name: ")
try:
    dest = open(destname, 'wb')
except Exception as e:
    print("Cannot create desination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dest.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    print(e.errno)

print(total, "bytes successfully written")
src.close()
dest.close



