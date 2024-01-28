#implementing all the functions in file handling

import os

def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write("Hello World!\n")
            print("File"+filename+"created successfully")
    except IOError:
        print("Error: could not create file"+filename)

def read_file(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except IOError:
        print("Error :could not read file"+filename)

def append_file(filename,text):
    try:
        with open(filename,'a') as f:
            f.write(text)
            print("Text appended to file"+filename+"successful")
    except IOError:
        print("Error cout not append to file"+filename)

def rename_file(filename,new_filename):
    try:
        os.rename(filename,new_filename)
        print("File"+filename+"renamed to"+new_filename)
    except IOError:
        print("Error: could not rename file"+filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File"+filename+"deleted successfully")
    except IOError:
        print("Error: could not delete file"+filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
    create_file(filename)
    read_file(filename)
    append_file(filename, "this is some additiona text\n")
    read_file(filename)
    rename_file(filename,new_filename)
    read_file(new_filename)
    delete_file(new_filename)
        