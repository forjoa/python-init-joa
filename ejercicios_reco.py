# contar del 1 al 10
lista_num = [10, 20, 30]

# for para recorrer una lista
for numero in lista_num:
    print(numero)
    
nombre = 'Joaquin'

# for para recorrer un string
for letra in nombre:
    print(letra)
    
    
# for por rangos
for cocacola in range(1, 11):
    print(cocacola)
    
numero_1 = 19
numero_2 = 25

if numero_1 == numero_2:
    print('Los números son iguales')
    
# Quiero saber si mi nombre contiene una A

mi_nombre = 'Joquin'

if 'a' in mi_nombre:
    print("La A se encuentra en tu nombre")
else:
    print("Tu nombre no tiene A")  




suma_total = 0

for i in range(1, 101):
    suma_total = suma_total + i
    
print(f'La suma total es: {suma_total}')

mi_palabra = 'america'

print(len(mi_palabra))


