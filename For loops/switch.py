"""
El switch es una herramienta que nos permite ejecutar 
diferentes secciones de código dependiendo de una condición. 
Se podia decir que Python no tenía un switch propio pero ahora se
puede considerar a "match" como uno.
"""

edad = input("¿Cuantos años tienes?\n> ")

match int(edad):
    case edad if edad >= 20:
        print("Eres un adulto")
    case edad if edad >= 10:
        print("Eres un joven")
    case edad if edad > 0:
        print("Eres un niño")
    case _:
        print("No nacido, yo qué sé")