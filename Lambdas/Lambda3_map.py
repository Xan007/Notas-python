enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))

print(cuadrados)

###

enteros = [1, 2, 3]

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def mitadDe(x):
    return x / 2

#Mapea con dos funciones
funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)


funciones = [lambda x: x, mitadDe] #X es el numero (e)
for e in enteros:
    valores = list(map(lambda x : x(e), funciones)) #X es una funcion
    print(valores)