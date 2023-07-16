"""
Ya aprendí sobre los usos basicos, pero hay más
"""

#3. Casos combinados

"""
Aqui simplemente se puede usar | que actua como or, si se cumple
una o la otra condicion
"""

def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Authentication error"
        case 404:
            return "Not found"
        case _:
            return "Other error"
        

#4. Wildcard in a list

"""
Aquí se usa en una lista. Verificamos si se cumple
el caso que damos. El * (asterisco) quiere decir que 
es todo lo demás que haya para la derecha (mas de uno)
"""

def alarm(item):
    match item:
        case [time, action]: #Solo si se cumple que hay dos elementos en la lista
            print(f'Good {time}! It is time to {action}!')
        case [time, *actions]: ###Actions viene siendo otra lista sin incluir el primer elemento pero si los demas
            print('Good morning!')
            for action in actions:
                print(f'It is time to {action}!')

alarm(['afternoon', 'work'])
alarm(['morning', 'have breakfast', 'brush teeth', 'work'])


#5. Sub patrones

"""
Se puede tener un patron dentro de otro patrón.

('morning' | 'afternoon' | 'evening') es un patron

quiere decir que busca alguno de todos esos en el primer elemento, ya que es un or.
Si no se cumple alguno de esos tres subpatrones nos pasa al caso default
"""

def alarm(item):
    match item:
        case [('morning' | 'afternoon' | 'evening'), action]:
            print(f'Good (?)! It is time to {action}!')
        case _:
            print('The time is invalid.')


"""
Por qué hay un (?). Porque no le tenemos una referencia al patron encontrado
Podemos añadir as, para crear una referencia con un nombre
"""

def alarm(item):
    match item:
        ###Ahora se puede acceder através de time, cualquiera de los 3 casos
        case [('morning' | 'afternoon' | 'evening') as time, action]:
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')


#6. Patrones condicionales

"""
Simplemente añadir un if.
"""

def alarm(item):
    match item:
        ##Busca, evening y action, solo si action no es work o study
        #De lo contrario lo manda al caso default de action
        case ['evening', action] if action not in ['work', 'study']:
            print(f'You almost finished the day! Now {action}!')

        #Solo si evening es el primero y fue rechazado anteriormente el action
        case ['evening', _]:
            print('Come on, you deserve some rest!')
        case [time, action]:
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')


#7. Matching objects

class Direction:
    def __init__(self, horizontal=None, vertical=None):
        self.horizontal = horizontal
        self.vertical = vertical

def direction(loc):
    match loc:
        case Direction(horizontal='east', vertical='north'):
            print('You towards northeast')
        case Direction(horizontal='east', vertical='south'):
            print('You towards southeast')
        case Direction(horizontal='west', vertical='north'):
            print('You towards northwest')
        case Direction(horizontal='west', vertical='south'):
            print('You towards southwest')
        case Direction(horizontal=None):
            print(f'You towards {loc.vertical}')
        case Direction(vertical=None):
            print(f'You towards {loc.horizontal}')
        case _:
            print('Invalid Direction')