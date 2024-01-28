#wirte a program to find factorial of n natural numbers

f = 1
n = int(input("Enter n value:"))

for i in range(1,n+1):
    f = f*i
print("Factorial of {} is {}".format(n,f))