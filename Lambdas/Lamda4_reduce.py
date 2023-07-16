#Suma de toda la lista

valores = [2, 4, 6, 5, 4]
suma = 0

for el in valores:
    suma += el

print(suma)

#Se puede hacer con la funcion reduce, pero toca importar un modulop

from functools import reduce

suma = reduce(lambda x, y: x + y, valores) 
print(suma)
