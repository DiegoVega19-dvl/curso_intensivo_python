from pathlib import Path
import json

numbers = [1,2,3,4,5,6,7,8]

path = Path('numbers.json') # si no existe el arhivo, lo crea
contenido = json.dumps(numbers) 
path.write_text(contenido) # alamcena el contenido en el archivo json