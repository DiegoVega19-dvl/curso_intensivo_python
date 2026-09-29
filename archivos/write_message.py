from pathlib import Path

contenido = "me gusta la programacion\n"
contenido += "me gusta crear nuevos juegos\n"
contenido += "y tambien me gusta trabajar con datos\n"

path = Path('archivos/programming.txt')

path.write_text(contenido)