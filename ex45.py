#program to print n prime numbers
n = int(input("Enter n value:"))

for j in range(2,n+1):
    flag1=0
    for i in range(2,j):
        if(j%i == 0):
            flag1 = 1
            break
    if(flag1 == 0):
        print(j)