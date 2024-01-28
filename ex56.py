#using both args and **kwargs

def myFun(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
    
args = ("Hemanth","sai","nag")
myFun(*args)

kwargs = {"arg1":"Hemanth","arg2":"Sai","arg3":"Nag"}
myFun(**kwargs)
print(type(args))
print(type(kwargs))