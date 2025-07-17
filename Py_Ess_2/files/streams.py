from os import strerror
import errno

try:
    s = open("C:/Users/Opeyemi/fela_Python/Py_Ess_2/nature/strings.py")
    # Actual processing goes here
    print("exists")
    s.close
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist")
    elif exc.errno == errno.EMFILE:
        print("You've opened too may files")
    else:
        print("The error number is: ", exc.errno)

try: 
    s = open("C:/Users/Opeyemi/fela_Python/Py_Ess_2/nature/string.py")
    # Actual processing goes here
    print("exists")
    s.close
except Exception as exc:
    print("The file could not be opened: ", strerror(exc.errno))

try:
    stream = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/streams.py", 'rb')
    print("this file exists")
    stream.close()
    streams = open("c:/Users/Opeyemi/fela_Python/Py_Ess_2/files/str.py", 'rb')
    print("this file exists")
    streams.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")





