#Assert se le debe dar una condición que si se cumple va continuar el programa normalmente
#Pero si la condicion no se cumple, va lanzar un error que podemos especificar

numero = 10

assert numero == 10

print("No paso nada porque la condicion se cumple")

#assert numero > 10

#Lanza un error de tipo AssertionError sin descripcion, para añadir descripcion se hace

assert numero > 10, "El numero debia ser mayor que 10"