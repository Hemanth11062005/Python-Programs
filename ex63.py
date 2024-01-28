#Exception handling using try except and else block

try:
    numerator = int(input("enter a number to divide:"))
    denominator = int(input("Enter a number to divide by"))
    result = numerator/denominator
    
except ZeroDivisionError as e:
    print(e)
    print("Don't divide by zero!")

except ValueError as e:
    print(e)
    print("Enter only numbers plz")

except Exception as e:
    print(e)
    print("Somthing went wrong")
    
else:
    print(result)

finally:
    print("This will always execute")
    