
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

    def fill_tank_gas(self, litros):
        print(f"el tanque tiene: {litros} listros de gasolina")


"""
# clase bateria
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(
            f"este carro tiene una bateria de: {self.battery_size} kmh de rendimiento")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(
            f"este carro puede ir alrededor de {range} millas con la carga completa")

    def upgrade_battery(self):
        print(f"el tamaño de la bateria es: {self.battery_size}")
        self.battery_size = 65
        print(f"mejorando la capacidad de la bateria a : {self.battery_size}")


# clase carro electrico
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # compisicion de la clase battery (objeto)

    def fill_tank_gas(self):
        print("los carros elctricos no tienen tanque de gasolina")


mi_carro = ElectricCar("toyota", "prius", 2026)
print(mi_carro.decribe_name())
mi_carro.battery.describe_battery()
mi_carro.battery.get_range()
mi_carro.battery.upgrade_battery()
mi_carro.battery.get_range()
"""
