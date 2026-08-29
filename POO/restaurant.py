class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """constructor"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # metodos
    def describe_restaurant(self):
        print(
            f"el restaurante se llama {self.restaurant_name} y es de comida {self.cuisine_type}")

    def open_restaurant():
        print("el restaurante esta abierto")


# creacion de instancias
ruta = Restaurant("ruta 66", "tex-mex")
birria = Restaurant("tex-mex", "mexicano")
hates = Restaurant("hates el may", "hotdogs")

print(ruta.describe_restaurant())
print(birria.describe_restaurant())
print(hates.describe_restaurant())
