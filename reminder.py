mi_dic = {
    "nombre": "Joaquin"
}

contador = {
    "perros": 10,
    "gatos": 20
}

print(f'{contador.keys()}')

for clave, valor in contador.items():
    print(f'{clave}: {valor}')
    

# funciones

# funciones que imprimen
# función de un solo parametro
def saludar(nombre: str):
    print(f'Hola, {nombre}')
    
saludar('Joaquin')

# función de más de un parametro
def sumar(numero_1: int, numero_2: int):
    print(f'La suma es: {numero_1 + numero_2}')
    
sumar(10,15)

# funciones que te DEVUELVEN algo
def restar(numero_1: int, numero_2: int):
    return numero_1 - numero_2

resultado = restar(10, 3)

print(f'La resta es: {resultado}')

# desestructuración
pizza= {'harina':150,'levadura':10,'agua':20,'mozzarella':65,'tomate':75}

print(pizza.items())

# [('harina', 150), ('levadura', 10), ('agua', 20), ('mozzarella', 65), ('tomate', 75)]
for clave, valor in pizza.items(): 
    print(clave, valor)
    
peso = sum(pizza.values())

print(f'El peso es: {peso}gr')

mas_pesado = max(pizza.values())

print(f'El más pesado es: {mas_pesado}gr')

menos_pesado = min(pizza.values())

print(f'El menos pesado es: {menos_pesado}gr')

print(eval('10+20+30'))
    

    




















