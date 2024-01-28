#file detection

import os

path = "E:\\python\\ex65.py"

if os.path.exists(path):
    print("This location exists")
    if os.path.isfile(path):
        print("this is a file")
        if os.path.isdir(path):
            print("this is a folder")
else:
    print("There is no path")