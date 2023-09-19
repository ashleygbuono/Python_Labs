from car import Car

car_1 = Car("Subaru", "Legacy", 2018, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

print(f'{car_1.make} {car_1.model}')
print(f'{car_1.year} {car_1.color}')

car_1.drive()
car_1.stop()


print(f'{car_2.make} {car_2.model}')
print(f'{car_2.year} {car_2.color}')

car_2.drive()
car_2.stop()