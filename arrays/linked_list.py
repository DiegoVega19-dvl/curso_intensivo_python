"""
las listas enlazadas son una coleccion de nodos, donde cada nodo
contiene dos partes
1.- un valor (dato almacenado)
2.- un puntero al nodo siguiente (referencia al siguiente puntero)

tipos de linked list

1.- simples
2.- doblemente enlazadas
3.- circulares
"""

class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.sig = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self,valor):
        nuevo = Nodo(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def esta_vacia(self):
        return self.cabeza is None

