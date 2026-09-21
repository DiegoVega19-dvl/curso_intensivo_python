from car import Car, ElectricCar

my_new_car = Car("honda", "civic", 2022)
my_new_car.odometer_reading = 500
print(my_new_car.read_odometer())
print(my_new_car.decribe_name())

my_leaf = ElectricCar("nissan","leaf",2022)
print(my_leaf.decribe_name())
my_leaf.battery.describe_battery()
