from name_function import get_formatted_name

print("ingresa 'q' para cerrar el programa")
while True:
    first = input("ingresa tu nombre: ")
    if first == "q":
        break

    last = input("ingresa tu apellido: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"nombre formateado: {formatted_name}")