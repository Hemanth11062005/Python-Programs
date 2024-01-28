from car import Car
    
car_1 = Car("Chervy","Corvette",2021,"blue")
car_2 = Car("Tesla","shippedin",2023,"grey")

print(car_1.model)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.model)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.stop()
car_2.drive()