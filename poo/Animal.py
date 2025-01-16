class Animal:
    def __init__(self, nombre: str, edad: int, peso: float):
        self.nombre = nombre,
        self.edad = edad
        self.peso = peso
        
    def mostrarInformacion(self):
        print(f'Mi nombre es {self.nombre}, mi peso es {self.peso}kg y mi edad es {self.edad} años')
        