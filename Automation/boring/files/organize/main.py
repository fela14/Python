import shutil, os
import send2trash

os.chdir('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\organize')
# shutil.copy('.\\spam.txt', '.\\copy')
# shutil.copy('.\\eggs.txt', '.\\copy\\eggs.bak')
# shutil.copytree('.\\bacon', '.\\pancetta')
# shutil.move('.\\eggs.txt', '.\\bacon')
# shutil.move('.\\spam.txt', '.\\bacon\\maps.txt')

"""
for filename in os.listdir():
    if filename.endswith('txt'):
        print(filename)   # advisable to print first before deleting
        os.unlink(filename)


trashFile = open('trash.txt', 'a')   # creates the file
trashFile.write('Bacon is not a vegetable')
trashFile.close()
send2trash.send2trash('trash.txt')   # better alternative to shutil

folder = 'C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\organize\\delicious'
os.chdir(folder)

for folderName, subFolders, fileNames in os.walk(folder):
    print('The current folder is: ',folderName)
    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
        for fileName in fileNames:
            print('FILE INSIDE ' + folderName + ': ' + filename)

import zipfile

os.chdir('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\organize')


with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')
print('example.zip')

exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

file1Info = exampleZip.getinfo('file1.txt')
file2Info = exampleZip.getinfo('file2.txt')
print(file1Info.file_size)
print(file2Info.file_size)
print(file1Info.compress_size)
print(file2Info.compress_size)
print('File is %x time(s) smaller' % ( round(file1Info.file_size/file1Info.compress_size)))

exampleZip = zipfile.ZipFile('example.zip')
os.chdir('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files')
exampleZip.extractall()
exampleZip.extract('file1.txt', 'C:\\Users\\Opeyemi\\fela_Python')
exampleZip.close()

"""
import zipfile

os.chdir('C:\\Users\\Opeyemi\\fela_Python\\Automation\\boring\\files\\organize')

with zipfile.ZipFile('new.zip', 'a') as nz:
    nz.write('new.txt', compress_type=zipfile.ZIP_DEFLATED)
print(nz.namelist())
newInfo = nz.getinfo('new.txt')
print(newInfo.file_size)
print(newInfo.compress_size)
print('The file was compressed by %x' % (round(newInfo.file_size/newInfo.compress_size)))

