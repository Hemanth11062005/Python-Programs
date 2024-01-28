# exception handling with using raise 

def example_function(value):
    if value<0:
        raise ValueError("Value must be non-negative zero")
    else:
        print(value)

try:
    example_function(-2)
except ValueError as ve:
    print("Caught an exception:",ve)