"""
La función incorporada enumerate() permite, como lo indica su nombre, enumerar una 
colección (por ejemplo, una lista, una tupla, o cualquier otro objeto iterable). 
Opera recibiendo como argumento cualquier objeto iterable y retornando uno nuevo 
cuyos elementos son tuplas de dos elementos: el primero, un índice (empezando por el cero); 
el segundo, el elemento que se encuentra en esa posición en el objeto iterable original.
"""

lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)

# Salida:
# 0 A
# 1 B
# 2 C

lista = ["A", "B", "C"]

en = list(enumerate(lista))
print(en)

# Salida;
# [(0, 'A'), (1, 'B'), (2, 'C')]