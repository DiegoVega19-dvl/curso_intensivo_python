"""contador = 0

while contador < 10:
    print(contador)
    contador += 1"""


"""promt = "el loop se detendra hasta que escribas 'fin': "

mensaje = ""
while mensaje != 'fin':
    mensaje = input(promt)
    print(mensaje)"""


"""promt = "el programa correra hasta que escribas 'fin' : "

active = True  # flag
while active:
    mensaje = input(promt)

    if mensaje == 'fin':
        active = False
    else:
        print(mensaje)"""


numero_actual = 0

while numero_actual < 100:
    numero_actual += 1
    if numero_actual % 2 == 0:
        continue

    print(numero_actual)
