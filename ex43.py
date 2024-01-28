#program to find given number is armstrogn or not

n = int(input("Enter n value:"))
sum = 0
temp = n
while(n!=0):
    r = n%10
    sum = sum +r*r*r
    n=n//10
if(sum == temp):
    print("Given number is armstrong number")
else:
    print("given number is not an armstrong number")