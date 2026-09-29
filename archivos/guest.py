from pathlib import Path

nombre = input("ingresa tu nombre completo: ")

root = Path("archivos/guest.txt")

root.write_text(nombre)