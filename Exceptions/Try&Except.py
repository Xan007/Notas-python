#Puntos importantes
#A try clause is executed up until the point where the first exception is encountered.
#Inside the except clause, or the exception handler, you determine how the program responds to the exception.
#You can anticipate multiple exceptions and differentiate how the program should respond to them.


import sys

try:
    print(1+ "Hola")
except:
    print("Hubo un error")


#Se ejecuta el bloque que hay en try hasta que suceda un error y luego se pasa a except

#Se puede capturar el error de esta forma

try:
    print(1+ "Hola")
except Exception as Error:
    print("Hubo un error")
    print(Error)


#Hay errores ya construidos dentro de Python que se puede detectar esepcificamente

#Por ejemplo de este error se llama TypeError y se puede especificar así

try:
    print(1+ "Hola")
except TypeError as Error:
    print("Hubo un error")
    print(Error)

#Otro ejemplo

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as Error:
    print(Error)

#En el bloque try pueden suceder más de 1 error, pero a penas detecte el primero va mandar al bloque except

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')

#Por ultimo nos encontramos con else que lo que hará es que si ningun error aparece, va correr ese bloque

#Tambien con finally que se va ejecutar si o si