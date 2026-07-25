# ordenar un lista

carros = ['honda', 'ford', 'audi', 'toyota']

# carros.sort(reverse=True)  # reverse = True lo ordena alreves de z-a
# print(carros)

# el metodo sort ordena una lista de forma alfabeticamente


'''con el metodo sorted() te entrega una lista temporal en lugar de modificar la lista original como lo hace sort'''

print(sorted(carros))
print(carros)

# con el metodo len pueden saber la longitud de una lista, osea cuantos items tiene una lista
print(len(carros))


# esto dara un IndexError
print(carros[4])
