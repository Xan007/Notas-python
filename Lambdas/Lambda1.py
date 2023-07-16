#La sintaxis es la siguiente
#lambda arguments : expression

#Son funciones anonimas, toma todos los argumentos que queramos pero solo tienen una expresión

x = lambda a, b, c : a + b + c
print(x(10, 5, 5))

#Se puede usar para crear una funcion dentro de otra funcion

def Multiplicador(n):
  return lambda a : a * n

DobleDe = Multiplicador(2)
TripleDe = Multiplicador(3)

print("El doble de {} es {}".format(3, DobleDe(3)))
print("El triple de {} es {}".format(4, TripleDe(4)))

def Elevar(n):
    return lambda a: a**n

CuadradoDe = Elevar(2)
CuboDe = Elevar(3)

print("El cuadrado de {} es {}".format(2, CuadradoDe(2)))
print("El cubo de {} es {}".format(4, CuboDe(4)))
