class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """constructor"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # metodos
    def describe_restaurant(self):
        print(
            f"el restaurante se llama {self.restaurant_name} y es de comida {self.cuisine_type}")

    def open_restaurant():
        print("el restaurante esta abierto")

    def set_number_served(self, number):
        self.number_served = number
        print(f"empezamos con {self.number_served} clientes")

    def increment_number_served(self, clientes):
        self.number_served += clientes
        print(
            f"esta movido el dia, llegaron... {self.number_served} clientes mas")


# creacion de instancias
ruta = Restaurant("ruta 66", "tex-mex")
birria = Restaurant("tex-mex", "mexicano")
hates = Restaurant("hates el may", "hotdogs")


print(ruta.describe_restaurant())
print(ruta.set_number_served(10))
print(ruta.increment_number_served(4))
print(birria.describe_restaurant())
print(birria.set_number_served(5))
print(birria.increment_number_served(6))
print(hates.describe_restaurant())
print(hates.set_number_served(7))
print(hates.increment_number_served(8))
