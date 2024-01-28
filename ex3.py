# Variables and Names
'''Now you can print things with print and you can do math. The next step is to learn about
variables. In programming, a variable is nothing more than a name for something so you
can use the name rather than the something as you code. Programmers use these variable
names to make their code read more like English and because they have lousy memories. If
they didn’t use good names for things in their software, they’d get lost when they tried to
read their code again.'''

cars = 100
space_in_car = 4.0
drivers = 30
passenges = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_car
average_passengers_per_car = passenges / cars_driven

print("There are",cars,"available now")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empyt car driven")
print("We have", passenges,"to carpool today")
print("We can transport",carpool_capacity,"people today")
print("We need to put about",average_passengers_per_car,"in each car")