def verificarPalabra(cadena):
    estado = 0
    for i, c in enumerate(cadena):
        if estado == 0:
            if c.isalpha() or c == '_':  # Permitir letras y '_' como primer carácter
                estado = 1
            else:
                estado = -1
                break
        elif estado == 1:
            if c.isalnum() or c == '_':
                estado = 1
            else:
                estado = -1
                break
    if estado == 1:
        print('Palabra aceptada')
    else:
        print(f'Carácter {c} no reconocido. rechazada')

# Ejemplo de uso:
cadena1 = "numero1"
verificarPalabra(cadena1)

cadena3 = "_suma2"
verificarPalabra(cadena3)

cadena4 = "n1_2"
verificarPalabra(cadena4)

cadena5 = "x3y4z_"
verificarPalabra(cadena5)

cadena6 = "5numero"
verificarPalabra(cadena6)

cadena7 = "m*2"
verificarPalabra(cadena7)

cadena8 = "_hola-hola"
verificarPalabra(cadena8)

cadena9 = "n1#abhskfqwerg"
verificarPalabra(cadena9)

cadena10 = "numero#"
verificarPalabra(cadena10)