#La sintaxis es:
#newlist = [expression for item in iterable if condition == True]

Nums = [x+1 for x in range(0, 30)]
DobleDeNums = [x*2 for x in Nums]

print(Nums)
print(DobleDeNums)

#Lo que primero se pone es el item que se va agregar, puede traer condiciones
#Luego viene el for loop 
#Luego (opcional) la condicion que debe cumplir

Impares = [x for x in Nums if x%2 != 0]
print(Impares)



"""
En diccionarios
"""

lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}