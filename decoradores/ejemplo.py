import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} s")
        return resultado
    return wrapper

@medir_tiempo
def procesar_datos(n):
    return sum(range(n))

procesar_datos(1_000_000)