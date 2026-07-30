pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(
    f'haz ordenado una pizza {pizza['crust']} con los siguientes ingredientes: ')

for toppings in pizza['toppings']:
    print(toppings)
