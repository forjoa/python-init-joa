#Pedir numero al usuario y de ese numero arrojar la tabla de multiplicar 
numero_tabla=input ('Inserte un numero\n')
numero_tabla= int(numero_tabla)
for cocacola in range(1,10) :
   print(f'{numero_tabla} x {cocacola} = {numero_tabla * cocacola}')