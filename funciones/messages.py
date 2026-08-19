

def show_messages(lista):
    for mensaje in lista:
        print(mensaje)


def send_messages(lista, send_messages):
    while lista:
        mensaje_actual = lista.pop()
        print(f"enviando mensaje: {mensaje_actual}")
        send_messages.append(mensaje_actual)


mensaje_lista = ['hola', 'como', 'estas']
mensaje_enviado = []
show_messages(mensaje_lista)

send_messages(mensaje_lista, mensaje_enviado)
