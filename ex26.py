#swapping of two numbers using third variable

a = int(input("Enter a:"))
b = int(input("Enter b:"))

print("Before Swapping \n a = {} b = {}".format(a,b))

c = a
a = b
b = c

print("After swapping a = {} b = {}".format(a,b))
