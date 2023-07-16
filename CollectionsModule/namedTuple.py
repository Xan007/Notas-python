from collections import namedtuple

#El segundo parametro que define el nombre de cada atributo
#Puede ser una lista [a, b, c]
#Puede ser un string "a b c" o "a, b, c"
#Puede ser un generador (field for field in "abc")
Punto = namedtuple("punto", ["x", "y"])
mi_punto = Punto(2, 3)
print(mi_punto.x, mi_punto[0])
print(mi_punto.y, mi_punto[1])


#Tambien se le puede añadir un valor por defecto si un atributo no es especificado
#defaults se hace de izquierda a derecha
Punto = namedtuple("punto", ["x", "y"], defaults=[0, 2])
mi_punto2 = Punto()

print(mi_punto2)

#Se puede crear un diccionario a partir de la tupla

print(mi_punto._asdict())

#Tambien se puede reemplazar un atributo, solo que este devuelve una tupla nueva
mi_punto2 = mi_punto2._replace(x=10)
print(mi_punto2)