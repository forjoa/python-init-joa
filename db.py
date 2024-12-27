usuario_verificar = input('Introduce el estudiante que quieres verificar\n')

estudiantes = {
    "Ana": [8, 9, 10], 
    "Luis": [7, 6, 8], 
    "Carlos": [9, 10, 10]
}

if usuario_verificar in estudiantes.keys():
    promedio = sum(estudiantes[usuario_verificar]) / len(estudiantes[usuario_verificar])
    print(f'El promedio de {usuario_verificar} es {promedio}')
else:
    print('El usuario no existe')
