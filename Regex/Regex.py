import re 

Patterns = {
    "Email": "[\w.-]+@[a-zA-Z]+\.(com|edu|net)",
    "PhoneNumber": "(\+\d\d?\-\d\d\d\d?|\+\d\d?\d?)\s([\d -]+)"
}

print("Inicio de sesión básico:")

Email = input("\n1. Introduce tu correo electronico: ")
PhoneNumber = input("2. Introduce tu numero telefonico: ")

#Verificar numero:

PhoneMatch = re.search(Patterns["PhoneNumber"], PhoneNumber)

if (PhoneMatch):
    print("Su codigo de país es: {}".format(PhoneMatch.group(1)))
    print("Su numero telefonico es: {}".format(re.sub("\s+", "", PhoneMatch.group(2))))

    print("\nNumero telefonico valido ✔")
else:
    print("\nNumero telefonico no valido ❌")

EmailMatch = re.search(Patterns["Email"], Email)

if (EmailMatch):
    print("\nCorreo electronico valido ✔")
else:
    print("\nCorreo electronico no valido ❌")
