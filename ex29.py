#Program to find roots of quadratic equation using control flow

import math
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
d = b*b - 4*a*c
if(d>0):
        x1 = (-b-math.sqrt(d))/(2*a)
        x2 = (-b+math.sqrt(d))/(2*a)    
        print("\n Roots are real Root1:",x1," Root 2", x2)
elif (d>0):
    x1 = (-b)/(2*a)
    x2 = -b/(2*a)
    print("\n Roots are equal Root:",x1,"\t root<",x2)
elif d<0:
     print("\nRoots are imaginary because total value is -ve")
    