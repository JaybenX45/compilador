def verificarPalabraReservada(cadena):
    estado = 0

    for c in cadena:
        if estado == 0:
            if c == 't':
                estado = 1
            else:
                estado = -1
                break
        elif estado == 1:
            if c == 'h':
                estado = 2
            else:
                estado = -1
                break
        elif estado == 2:
            if c == 'e':
                estado = 3
            else:
                estado = -1
                break
        elif estado == 3:
            if c == 'n':
                estado = 4
            else:
                estado = -1
                break

    if estado == 4 and len(cadena) == 4:
        print('Palabra aceptada')
    else:
        print('Palabra rechazada')

# Ejemplo de uso:
cadena = "then"
verificarPalabraReservada(cadena)  

cadena = "then+"
verificarPalabraReservada(cadena)  

cadena = "thenkjvj"
verificarPalabraReservada(cadena)  

cadena = "the"
verificarPalabraReservada(cadena)  

cadena = "t"
verificarPalabraReservada(cadena)