#clousures

def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of

square = nth_power(2)
print(square(2))
print(square(3))
print(square(4))

cube = nth_power(3)
print(cube(2))
print(cube(3))
print(cube(4))