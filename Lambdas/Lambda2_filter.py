mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, mi_lista))

print(pares)


numeros = [x+1 for x in range(0, 100)]
divisiblesEn10 = list(filter(lambda x: x%10 == 0, numeros)) #Si o si la funcion anonima (lambda) debe devolver un valor booleano

print(divisiblesEn10)