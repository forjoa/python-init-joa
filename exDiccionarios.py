"""lista_personas = [
    {
        "id": 1,
        "nombre": "Joaquin",
        "edad": 21,
        "ciudad": "Madrid"
    },
    {
        "id": 2,
        "nombre": "Pepe",
        "edad": 20,
        "ciudad": "Barcelona"
    },
]"""

yo = {
    "id": 1,
    "nombre": "Joaquin",
    "edad": 21,
    "ciudad": "Madrid"
}


for clave, valor in yo.items():
    print(f'{clave.upper()}: {valor}')

