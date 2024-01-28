#program to find reverse number of given numbers

'''
input = 245
output = 542
'''

n = int(input("Enter n value:"))
sum = 0
while(n!=0):
    r = n%10
    sum = sum*10+r
    n = n//10
print("sum of digits:",sum)