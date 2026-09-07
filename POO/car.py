
# clase padre
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def decribe_name(self):
        long_name = f"{self.make}, {self.model}, {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"este carro tiene {self.odometer_reading} millas de uso")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("no puede modificar las millas del carro")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# clase carro electrico
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


mi_carro = ElectricCar("toyota", "prius", 2026)
print(mi_carro.decribe_name())
