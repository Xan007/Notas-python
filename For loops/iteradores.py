"""
Se podría explicar la diferencia entre iteradores e iterables usando un libro como analogía. 
El libro sería nuestra clase iterable, ya que tiene diferentes páginas a las que podemos acceder.
Por otro lado, el iterador sería un marcapáginas, es decir, una referencia que nos indica en qué 
posición estamos del libro, y que puede ser usado para “navegar” por él.
"""

"""
Se va accediendo secuencialmente a los elementos hasta que la excepción StopIteration es lanzada. 
Dicha excepción se lanza cuando hemos llegado al final, y no existen más elementos que iterar.
"""

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)

print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))