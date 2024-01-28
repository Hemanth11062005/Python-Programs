#swapping of two numbers without using third variable

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

print("Before swap {} and {}".format(a,b))

a = a+b
b = a-b
a = a-b

print("After swap a {} b {}".format(a,b))