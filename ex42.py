#program to find given number is pallindrome or not
n = int(input("Enter n value:"))
rev = 0
temp = n
while(n!=0):
    r = n%10
    rev = rev*10 + r
    n = n//10
print(rev)
print(temp)
if(temp == rev):
    print("Given number is pallindrome")
else:
    print("Given number is not pallindrome")