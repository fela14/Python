import platform
import os

# print(os.uname())  -> only on Unix systems
print(platform.uname())
print(os.name)

"""
os.mkdir('my_first_directory')
print(os.listdir())

os.makedirs('my_first_dir/my_second_dir')
os.chdir('my_first_dir')
print(os.listdir())

os.makedirs('my_first_dir/my_second_dir')
os.chdir('my_first_dir')
print(os.getcwd())
os.chdir('my_second_dir')
print(os.getcwd())

os.mkdir('my_first_dir')
os.listdir()
os.rmdir('my_first_dir')
os.listdir

os.makedirs('my_first_dir/my_second_dir/my_third_dir')
print(os.listdir())
os.removedirs('my_first_dir/my_second_dir/my_third_dir')
print(os.listdir())

returned_value = os.system('mkdir my_first_dir')
print(returned_value)
"""

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            return
        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)

directory_searcher = DirectorySearcher()
directory_searcher.find("./Py_Ess_2", "generators")
        
