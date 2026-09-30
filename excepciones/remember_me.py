from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contenido = path.read_text()
        username = json.loads(contenido)
        return username
    else:
        return None

def get_new_user(path):
    username = input("¿cual es tu nombre?: ")
    contenido = json.dumps(username)
    path.write_text(contenido)
    return username


def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"bienvenido de regreso, {username}")
    else:
        username = get_new_user(path)
        print(f"te recordaremos cuando regreses, {username}!")

greet_user()