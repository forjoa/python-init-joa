numero = input("Escribe tu número\n")
# devolver si el número es negativo, positivo o cero

# pasar el número a Integer
numero = int(numero)

if numero > 0:
    print('número positivo')
elif numero < 0:
    print('número negativo')
else:
    print('número es igual a cero')