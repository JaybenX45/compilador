def ft_numero(cad):
    estado = 0
    lexema = ""
    decimal = False
    exponente = False

    for arco in cad:
        if estado == 0:
            if arco.isdigit():
                estado = 1
                lexema += arco
            elif arco == '-':
                estado = 2
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

    if estado in (1, 4, 8):
        if exponente:
            return "NUMERO ACEPTADO", lexema
        elif decimal:
            return "NUMERO ACEPTADO", lexema
        else:
            return "NUMERO ACEPTADO", lexema
    else:
        return "No ACEPTADO", lexema

# Ejemplos de verificación
#print(ft_numero("1234E+5"))
#print(ft_numero("3.14"))
#print(ft_numero("2.5E+10"))
#print(ft_numero("1E-9"))
#print(ft_numero("123.45E++"))

#exitosos5#
cadena1 = "1234E+5#gwjqhgdj"
resultado, lexema = ft_numero(cadena1)
print(resultado)

cadena2 = "23E-243"
resultado, lexema = ft_numero(cadena2)
print(resultado)
cadena3 = "0.3456##"
resultado, lexema = ft_numero(cadena3)
print(resultado)
cadena4 = "10.11E12"
resultado, lexema = ft_numero(cadena4)
print(resultado)

#no reconocidos
cadena5 = "+123"
resultado, lexema = ft_numero(cadena5)
print(resultado)
cadena6 = "123EE"
resultado, lexema = ft_numero(cadena6)
print(resultado)
cadena7 = "123.45E++"
resultado, lexema = ft_numero(cadena7)
print(resultado)