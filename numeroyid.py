def ft_numero(cad):
    estado = 0
    lexema = ""
    decimal = False
    exponente = False
    identificador = True  # Indica si el lexema es un identificador

    for arco in cad:
        if estado == 0:
            if arco.isdigit():
                estado = 1
                lexema += arco
            elif arco == '-':
                estado = 2
                lexema += arco
            elif arco.isalpha() or arco == '_':
                estado = 9  # Identificador
                lexema += arco
            else:
                estado = 5  # Estado de error
        elif estado == 1:
            if arco.isdigit():
                lexema += arco
            elif arco == '.':
                estado = 3
                lexema += arco
                decimal = True
            elif arco in ('E', 'e'):
                estado = 4
                lexema += arco
                exponente = True
            elif not arco.isalnum():
                break
        elif estado == 2:
            if arco.isdigit():
                estado = 1
                lexema += arco
            elif arco == '.':
                estado = 3
                lexema += arco
                decimal = True
            else:
                estado = 5
        elif estado == 3:
            if arco.isdigit():
                estado = 4
                lexema += arco
            elif not arco.isalnum():
                break
        elif estado == 4:
            if arco.isdigit():
                lexema += arco
            elif arco in ('E', 'e'):
                estado = 6
                lexema += arco
                exponente = True
            elif not arco.isalnum():
                break
        elif estado == 6:
            if arco in ('+', '-'):
                estado = 7
                lexema += arco
            elif arco.isdigit():
                estado = 8
                lexema += arco
            else:
                estado = 5
        elif estado == 7:
            if arco.isdigit():
                estado = 8
                lexema += arco
            else:
                estado = 5
        elif estado == 8:
            if arco.isdigit():
                lexema += arco
            elif not arco.isalnum():
                break
        elif estado == 9:  
            if arco.isalnum() or arco == '_':
                lexema += arco
            else:
                break

    if estado in (1, 4, 8):
        if exponente:
            return "NUMERO ACEPTADO", lexema
        elif decimal:
            return "NUMERO ACEPTADO", lexema
        else:
            return "NUMERO ACEPTADO", lexema
    elif estado == 9:
        return "ID ACEPTADO", lexema
    else:
        return "No ACEPTADO", lexema
        
cadena1 = "1234E+5#"
resultado, lexema = ft_numero(cadena1)
print(resultado)  

cadena2 = "+123"
resultado, lexema = ft_numero(cadena2)
print(resultado)

cadena3 = "_sum"
resultado, lexema = ft_numero(cadena3)
print(resultado)

cadena4 = "variable_123"
resultado, lexema = ft_numero(cadena4)
print(resultado) 