"""
Una clase iterable es una clase que puede ser iterada. Dentro de Python hay gran 
cantidad de clases iterables como las listas, strings, diccionarios o ficheros. 
Si tenemos una clase iterable, podemos usarla a la derecha del for de la siguiente manera.

for elemento in [clase_iterable]:

la variable elemento ira tomando valores distintos por cada elemento de la clase
iterable.
"""


"""
¿Como hago mi clase iterable?
"""

class MiClase:
    def __init__(self, items):
        self.lista = items

    """
    Por otro lado, el método __iter__() devuelve un iterador, 
    que simplemente es el iterador de la propia lista. 
    """
    def __iter__(self):
        return iter(self.lista)
    

miobjeto = MiClase([5, 4, 3])
for item in miobjeto:
    print(item)