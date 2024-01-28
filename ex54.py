#argv non - variable parameters

def myFun(*args):
    for arg in args:
        print(arg,end=" ")
        
myFun("Hello","Welcome","to","python tutorials")