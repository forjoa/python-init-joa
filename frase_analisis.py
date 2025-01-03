"""
Entrada: clasificar_palabras("El día es soleado y yo estoy muy feliz")
Salida: {2: ['El', 'yo'], 3: ['día', 'muy'], 8: ['soleado'], 5: ['estoy', 'feliz']}
"""

def clasificar_palabras(texto: str):
    lista_palabras = texto.split()
    contador_palabras = {}
    for palabra in lista_palabras:
        longitud_palabra = len(palabra)
        if longitud_palabra in contador_palabras: # verificar si la longitud existe
            contador_palabras[longitud_palabra].append(palabra) # agregar la nueva palabra a la lista existen
        else: # si no existe la longitud
            contador_palabras[longitud_palabra] = [palabra] # creamos la lista con la única palabra
    return contador_palabras

print(clasificar_palabras("El día es soleado y yo estoy muy feliz"))

        