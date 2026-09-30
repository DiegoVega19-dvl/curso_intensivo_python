from pathlib import Path



def count_words(path):
    """funcion para contar las palabras de un archivo"""
    try:
        contenido = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"lo sentimos, el archivo {path} no existe!!!")
    else:
        words = contenido.split()
        line = "the"
        num_words = words.count(line)
        print(f"el archivo {path}, tiene alrededor de {num_words} 'the' en todo el libro")


libros = ["alice.txt", "moby_dick.txt","pinocchio.txt", "siddharta.txt"]


for libro in libros:
    path = Path("excepciones") / libro
    count_words(path)