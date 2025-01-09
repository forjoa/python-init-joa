contactos = {"Juan": "123456789", "María": "987654321", "Ana": "555666777"}
nombre_contacto = input("Tu nombre").strip()

if nombre_contacto in contactos:
    print(contactos[nombre_contacto]) 
else: 
    print("el contacto no existe")