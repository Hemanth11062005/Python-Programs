#program to find number is pallindrome or not

n = int(input("Enter n value:"))
flag = 0
for i in range(2,n):
    r = n%i
if(r==0):
    flag =1
if(flag==0):
    print("n is a prime number:")
else:
    print("It is not a prime number")