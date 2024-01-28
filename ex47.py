#program to print n terms of fibonnacci series
n = int(input("Enter n value:"))
f1 = 0
f2 =1
print(f1," ",f2)
for i in range(1,n-1):
    f3= f1+f2
    print(f3)
    f1=f2
    f2=f3