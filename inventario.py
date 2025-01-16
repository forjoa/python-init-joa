INVENTARIO = {"manzanas": 10, "naranjas": 5, "plátanos": 8}

def mostrar_inventario():
    for clave, valor in INVENTARIO.items():
        print(f'{clave}: {valor}')
        
def agregar_producto(nombre, cantidad):
    INVENTARIO[nombre] = cantidad
    
def eliminar_producto(nombre):
    del INVENTARIO[nombre]

mostrar_inventario()  
# manzanas: 10  
# naranjas: 5  
# plátanos: 8  

agregar_producto("uvas", 15)  
mostrar_inventario()  
# uvas: 15  

eliminar_producto("naranjas")  
mostrar_inventario()  
# manzanas: 10  
# plátanos: 8  

