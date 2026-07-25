
squares = []

for values in range(20):
    square = values ** 2
    squares.append(square)

print(squares)


ejemplo = list(range(1, 10))
print(ejemplo)


# compresion de listas

cuadrado = [value**2 for value in range(1, 11)]
print(cuadrado)


# copying list

comida = ['tacos', 'pizza', 'sushi']

comida_copia = comida[:]

comida.append('ramen')

print(comida)
print(comida_copia)

ejemplo_tupla = (0,)
print(type(ejemplo_tupla))


# ejemplo tuplas

ejemplo_comida = ('pizza', 'tacos', 'sushi', 'hamburguesa')

for comida in ejemplo_comida:
    print(comida)
