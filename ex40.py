#find the sum of digits of given numbers example input 1234 outptu 1+2+3+4 = 10

n = int(input("Enter value:"))
temp = n
sum =0
while(n!=0):
    r = n%10
    sum = sum + r
    n = n//10
print("Sum of {} is {}".format(temp,sum))