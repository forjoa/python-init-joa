palabras = ["sol", "estrella", "luz", "planeta", "galaxia"]
contador = 0

for palabra in palabras:
    if len(palabra) > 4:
        print(palabra)
        contador = contador + 1 
        
print(f"Se encontraron {contador} palabras con más de 4 letras")