if __name__ == "__main__":
    abecedario = ""
    # Generar el abecedario con mayúsculas
    for i in range(65, 91):
        abecedario += chr(i)
    # Agregamos la Ñ, el espacio, el punto, la coma, el signo de interrogación y el signo de exclamación
    abecedario += "Ñ .,?!"
    
    mensaje = "El aguila esta en el nido"
    clave = "clave"
    cifrado = ""  # mensaje cifrado con la clave (aplicar XOR)
    mensaje_original = ""  # mensaje cifrado descifrado con la clave (volver a aplicar XOR)

    # Convertir el mensaje y la clave en mayusculas
    mensaje = mensaje.upper()
    clave = clave.upper()

    # Realizar el cifrado XOR entre el mensaje y la clave
    for i in range(len(mensaje)):
        # Obtener el índice de cada caracter en el abecedario
        letra_mensaje = mensaje[i]
        letra_clave = clave[i % len(clave)]
        
        # Comprobar si los caracteres están en el abecedario
        if letra_mensaje not in abecedario or letra_clave not in abecedario:
            continue  # Si el caracter no está en el abecedario, ignoramos este caracter

        # Obtener los índices de los caracteres en el abecedario
        index_mensaje = abecedario.index(letra_mensaje)
        index_clave = abecedario.index(letra_clave)
        
        # Aplicar XOR entre los índices
        index_cifrado = index_mensaje ^ index_clave
        
        # Añadir al mensaje cifrado
        cifrado += abecedario[index_cifrado]

    # Realizar el descifrado (aplicar XOR nuevamente con la misma clave)
    for i in range(len(cifrado)):
        letra_cifrada = cifrado[i]
        letra_clave = clave[i % len(clave)]
        
        if letra_cifrada not in abecedario or letra_clave not in abecedario:
            continue  # Ignorar caracteres no válidos

        index_cifrado = abecedario.index(letra_cifrada)
        index_clave = abecedario.index(letra_clave)
        
        # Aplicar XOR entre los índices
        index_descifrado = index_cifrado ^ index_clave
        
        # Añadir al mensaje original (descifrado)
        mensaje_original += abecedario[index_descifrado]

    # Output esperado
    print(f"input: {mensaje}")  # EL AGUILA ESTA EN EL NIDO
    print(f"output: {cifrado}")  # GA VCWDLV!GZTV!GG RPZGIWK
    print(f"output: {mensaje_original}")  # EL AGUILA ESTA EN EL NIDO

