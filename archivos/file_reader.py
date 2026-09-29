from pathlib import Path

path = Path('archivos/pi_digitos.txt')
# concatenacion de metodos
contenido = path.read_text() # rstrips quita los espacios en blanco

lineas = contenido.splitlines()

pi_string = ''

for linea in lineas:
    pi_string += linea.lstrip()

birdthday = input("ingresa tu fecha de cumpleaños en formato mmddyy: ")

if birdthday in pi_string:
    print("tu fecha de cumpleaños aparece en el primer millon de pi")
else:
    print("tu fecha de nacimiento no parace en el primer millon de pi")

"""
print(f"{pi_string[:8]}...")
print(len(pi_string))
print(type(pi_string))
"""


