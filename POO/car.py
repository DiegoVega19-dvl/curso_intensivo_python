class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def decribe_name(self):
        long_name = f"{self.make}, {self.model}, {self.year}"
        return long_name.title()


mi_nuevo_carro = Car("toyota", "corolla", 1986)

print(mi_nuevo_carro.decribe_name())
