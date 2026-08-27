
def make_pizza(size, *toppings):
    print(f"haciendo una pizza {size}, con los siguientes ingredientes:")
    for topping in toppings:
        print("-", topping)
