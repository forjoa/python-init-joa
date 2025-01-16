from Animal import Animal

animal_1 = Animal("Forky", 5, 4.5)
animal_2 = Animal("Pancho", 5, 4.5)

animal_1.mostrarInformacion()
animal_2.mostrarInformacion()

print(animal_1.nombre)
animal_1.nombre = 'Forky2'

animal_1.mostrarInformacion()