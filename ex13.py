
#how to take multiple inputs
#using List comprehension

x,y = [int(x) for x in input("Enter two values:").split()]
print("Number1 {} and Number2 {}".format(x,y))

x = [int(x) for x in input("Enter multiple values:").split(",")]
print("List of numbers",x)

