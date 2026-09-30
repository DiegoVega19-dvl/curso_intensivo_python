# division calculator

print("dame dos numeros, y hare una division")
print("ingresa 'q' para salir")

while True:
    numero = input("ingresa un numero: ")
    if numero == "q":
        break

    numero2 = input("ingresa otro numero: ")
    if numero2 == "q":
        break

    try:
        respuesta = int(numero) / int(numero2)
    except ZeroDivisionError:
        print("las divisiones entre 0 no se pueden!!!")
    except ValueError:
        print("debes ingresar solo numeros!!!")
    else:
        print(f"las respuesta es: {respuesta}")