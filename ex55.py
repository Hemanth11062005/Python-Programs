#**kwargs variable parameters

def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s"%(key,value))

myFun(first="Hemanth",mid="sai",last="nag")