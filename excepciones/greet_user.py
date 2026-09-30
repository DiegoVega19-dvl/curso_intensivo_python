from pathlib import Path
import json

path = Path("username.json")
contenido = path.read_text()
username = json.loads(contenido)

print(f"hola de vuelta, {username}")