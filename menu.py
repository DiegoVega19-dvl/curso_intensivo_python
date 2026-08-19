"""
menu de seleccion de conversiones fisicas

"""

while True:
    print("Bienvenido")
    print("1.- KMh a Ms")
    print("2.- grados C a F")
    print("3.- kg a Lb")
    print("4.- metros a pies")
    print("5.- salir del programa")

    opcion = int(input("selecciona una opcion (numero): "))

    match opcion:
        case 1:
            print("seleccionanste KMh a Ms")
            km = int(input("ingresa los km a convertir: "))
            m = km / 3.6
            print(f"{km} KMh es igual a {m} M/s")
        case 2:
            print("seleccionaste grados C a F")
            c = int(input("ingresa la cantidad de grados C°: "))
            f = (c * 1.8) + 32
            print(f"{c}C° es igual {f}F° ")
        case 3:
            print("seleccionaste kg a Lb")
            kg = int(input("ingresa la cantidad de kg: "))
            lb = kg * 2.20462
            print(f"{kg}kg es igual a {lb}lb")
        case 4:
            print("seleccionaste metros a pies")
            metros = float(input("ingresa los metros: "))
            pies = metros * 3.28084
            print(f"{metros}m es igual a {pies} pies")
        case 5:
            print("saliendo del programa...")
            break
        case _:
            print("ingresa una opcion disponible...")
