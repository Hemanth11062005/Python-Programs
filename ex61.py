#nested functions

def outerFunction(text):
    
    def innerFunction():
        print(text)
    innerFunction()

if __name__ == '__main__':
    outerFunction("Hey!")