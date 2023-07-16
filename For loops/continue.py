"""
continue se salta todo el código restante en la iteración actual 
y vuelve al principio en el caso de que aún queden iteraciones por completar.
"""

numeros = [i for i in range(1, 50)]

for num in numeros:
    if num%2 == 0:
        print(f"{num} par")
        continue

    print(f"{num} no par")