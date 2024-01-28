#swapping of two numbers using bitwise operators

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

print("Before swap a {} b {}".format(a,b))

a = a^b
b = a^b
a = a^b
print("After swap a {} and b {}".format(a,b))