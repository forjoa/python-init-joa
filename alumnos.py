CONTACTOS = {"Juan": "123456789", "María": "987654321"}

buscar_contacto("Juan")  
# Resultado: "123456789"

agregar_contacto("Ana", "555666777")  
mostrar_contactos()  
# Juan: 123456789  
# María: 987654321  
# Ana: 555666777

eliminar_contacto("María")  
mostrar_contactos()  
# Juan: 123456789  
# Ana: 555666777
