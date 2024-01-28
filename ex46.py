#program to find gcd of two numbers
x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
if(x==0):
    print("GCD is:",x)
elif(y==0):
    print("GCD is:",y)
elif(x==y):
    print("GCD is:",x)
else:
    while(x!=y):
        if(x>y):
            x = x-y
        else:
            y = y-x
    print("GCD is:",x)