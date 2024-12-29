print("Comentarios")

#Esto es un comentario de una sola línea 

"""
Esto
es
un
comentario
de
varias 
lineas

"""

print("Los comentarios no se han ignorado en consola")


# Ejemplo 1:
"""
Es una buena práctica documentar funciones, métodos o clases utilizando docstrings
(documentación dentro de comillas triples).
Por ejemplo:
"""
def suma(a, b):
    """
    Esta función calcula la suma de dos números.
    
    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: Resultado de sumar a y b
    """
    return a + b

print(suma(5,6))

# help(suma) # con esta función se puede mostrar en consola los comentarios que hemos añadido a la clase


