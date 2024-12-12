"""
Lista:
Mutable
Admite combinación de tipos de datos
"""
lista_edades = [40, 20, 30, 23, 34, 35]

print(f'Primera posición: {lista_edades[0]}') # primera posición

print(f'Lista completa sin cambios: {lista_edades}')

lista_edades[1] = 18 # modificando un valor en particular

print(f'Lista modificada: {lista_edades}')

lista_edades.append(100) # añadir un valor al final de la lista

print(f'Lista con un nuevo valor: {lista_edades}')

lista_edades.pop() # quitamos el último valor

print(f'Lista sin el último valor: {lista_edades}')



























# tuplas
mi_tupla = ()