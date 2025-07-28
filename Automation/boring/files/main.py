import os
path = os.path.join('usr', 'bin', 'spam')
print(path)

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\Workspace', filename))

print(os.getcwd())
os.chdir('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring')
print(os.getcwd())

# os.makedirs('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles')

print(os.path.abspath('.'))
print(os.path.abspath('main.py'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\Users\\Opeyemi'))
print(os.getcwd())

path = 'C:\\Users\\Opeyemi\\fela_Python\\Automation'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.dirname(path), os.path.basename(path))

print(path.split(os.path.sep))
print('C:\\Users\\Opeyemi\\fela_Python\\Automation'.split(os.path.sep))

print(os.path.getsize('C:\\Users\\Opeyemi'))
print(os.listdir(path))

totalSize = 0
for filename in os.listdir('C:\\Users\\Opeyemi'):
    print(os.path.join('C:\\Users\\Opeyemi', filename))
    totalSize += os.path.getsize(os.path.join('C:\\Users\\Opeyemi', filename))
print(totalSize)

print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\Users'))
print(os.path.exists('C:\\Some_made_up_folder'))
print(os.path.isfile('C:\\Users'))
print(os.path.isdir('C:\\Windows'))
print(os.path.isfile('C:\\Users'))

os.path.exists('D:\\') # checks for a flashdrive with the volume named D:\

helloFile = open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\hello.txt')
print(helloFile.read())

sonnetFile = open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\sonnet.txt')
print(sonnetFile.read())

# baconFile= open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\bacon.txt', 'w')
# baconFile.write('Hello world!\n')
# baconFile.close()

baconFile = open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable\n')
baconFile.close()

baconFile = open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

import shelve
shelfFile = shelve.open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\shelve\\data')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\shelve\\data')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\waffles\\shelve\\data')
shelfList1 = list(shelfFile.keys())
shelfList2 = list(shelfFile.values())
print(shelfList1)
print(shelfList2)

print(os.getcwd())

import pprint

# Step 1: Define your data
cat = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

# Step 2: Pretty format it into a string
cat_string = pprint.pformat(cat)

# Step 3: Write it to a .py file as a variable assignment
file_path = 'C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\cats.py'
fileObj = open(file_path, 'w')  
fileObj.write('cat = ' + cat_string + '\n')
fileObj.close()

# Step 4: Import the data from the newly written file
# import sys
# sys.path.append('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files')  # Ensure import path includes the folder

import cats

# Step 5: Access the data
print(cats.cat)               # Entire list
print(cats.cat[0])            # First dictionary
print(cats.cat[0]['name'])    # Value of 'name' in first dict



