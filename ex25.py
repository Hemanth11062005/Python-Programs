#program to find seconds in hours,min

a = int(input("Enter how many seconds"))
b = a//60
r1 = a%60
print("No of hours and seconds remaining:",b,r1)

c = a//3600
r2= a%3600

print("No of hours",c ,"and seconds remaining:",r2)