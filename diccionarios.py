# dictionary
mi_diccionario = {
    "nombre": "joaquin",
    "edad": 21,
    "ciudad": "madrid"
}

print(f'Mi nombre: {mi_diccionario["nombre"]}')

mi_diccionario["nombre"] = 'forky'

print(f'Mi nombre actualizado: {mi_diccionario["nombre"]}')

mi_diccionario["profesion"] = "programador"

print(f'Usuario con profesión: {mi_diccionario}')

del mi_diccionario["ciudad"]

print(f'Usuario sin ciudad: {mi_diccionario}')
