"""
Si pasamos dos listas a zip como entrada, 
el resultado será una tupla donde cada elemento 
tendrá todos y cada uno de los elementos i-ésimos de las pasadas 
como entrada.

En otras palabras:

(
    primer elemento de la primera lista,
    primer elemento de la segunda lista
)
"""

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))



"""
Se puede usar para iterar dos listas al mismo tiempo (en paralelo)
Incluso hasta más de dos listas <3
"""

posiciones = ["Primero", "Segundo", "Tercero"]
objetos = ["Manzana", "Platano", "Sandía"]

for pos, obj in zip(posiciones, objetos):
    print(f"{pos}. {obj}")


"""
zip() con diferentes longitudes

En este caso lo que pasará es que el iterador para cuando la lista más pequeña se acaba.
"""

numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]

for n, e in zip(numeros, espanol):
    print(n, e)


"""
zip() con diccionario


Toman los valores de las key del diccionario. Tal vez algo no demasiado interesante.
Si hacemos uso de la función items, podemos acceder al key y value de cada elemento.
"""

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}


##A la izquierda siempre el primer argumento que se pasa a zip()
for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three

"""
Deshacer el zip()
"""

c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')


"""
* es usado como unpacking en python
"""