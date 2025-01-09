# Número perfecto: aquel número que la suma de sus dividores son igual a ese número
# 6 -> 1 + 2 + 3 = 6
numero = 8128

# Output: no es perfecto | es perfecto
suma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i
        
if numero == suma_divisores:
    print('es un número perfecto')
else:
    print('no es un número perfecto')
    
# funcion que imprima si es perfecto o no es
def es_perfecto(numero: int):
    print()