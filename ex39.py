#find power of x of y without using math.pow() function

x = int(input("Enter x:"))
y = int(input("Enter y:"))
f = 1
for i in range(1,y+1):
    x = x*x
    
print("{} power {} is".format(x,y))