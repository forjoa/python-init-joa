lista_numeros = [10, 20, 30, 40, 13, 26, 89, 74, 125, 65]

mayor = 0

for numero in lista_numeros:
    if numero > mayor:
        mayor = numero
    
print(f'El número mayor es: {mayor}')