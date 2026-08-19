
# funcion con n arugmentos

def make_pizza(*toppings):
    print("\npreparando la pizza con los siguientes ingredientes:")
    for topping in toppings:
        print("-", topping)


make_pizza("peperoni")
make_pizza("salami", "jamon", "champiñones")
