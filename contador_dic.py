frase = "la programación es divertida y la programación es útil"
palabras = frase.split()
frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
print(frecuencias)
