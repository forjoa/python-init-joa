palabra = input('Elige una palabra')

def traducir(w):
    diccionario = {"hello": "hola", "world": "mundo", "apple": "manzana", "book": "libro", "dog": "perro"}
    print(diccionario[w])

traducir(palabra)