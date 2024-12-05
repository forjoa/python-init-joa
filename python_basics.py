

print("Hello world!")

'''
este es un comentario
'''

print(type(print))
print(type(1))
print(type(1.0))
print(type('hola'))
print(type(True))

# variables
print('variables')
name = 'joaquin'
print(type(name))

name = 1
print(type(name))

age: int = 20
print(type(age))
age = 'hola'
print(type(age))

# input
name = input('cómo te llamas?\n')
print('hola', name)

# string
print('string')

product_name = 'manzana'
quantity = 5

print('ha comprado' + ' ' + str(quantity) + ' ' + product_name)
print('ha comprado {} de {}'.format(quantity, product_name))
print(f'ha comprado {quantity} de {product_name}')
print('ha comprado', quantity, 'de', product_name)

address = 'calle de la fantasia 13 4d'
print(address)
print(address[0])
print(address[2:6])
print(address[2:])
print(address[:6])
print(address[-2])
print(address[::-1])

print('hola' > 'holb')
