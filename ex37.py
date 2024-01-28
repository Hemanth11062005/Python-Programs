#program to find sum of natural numbers upto n using while loop

sum = 0
n = int(input("Enter n value:"))
i = 1
while(i<=n):
    sum = sum + i
    i = i+1
print("Sum of {} natural number is {}".format(n,sum))