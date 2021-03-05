import re

print("---------------------------------------")

verdadero = lambda x: 'Lexema valido' if x else 'Lexema No valido'

""" cadena = [22015, 2068, 16.03, "hola 450"]
cadena2 = [52154, 1232, 0.265, "jejejej", 560]
print("")
print("3. Números enteros al inicio una línea: ")
print("")
print("Lexemas: " + str(cadena2))
print("") """
""" for i in cadena2:
    respuesta = re.search('\d+(\.\d+)$', str(i))
    if respuesta:
        #if (i%2 == 0):
        print("Lexema: " + str(i) + " Línea: " + str(respuesta.start()) + " Columna: " + str(respuesta.end()))
    else:
        print("Lexema no valido") """

cadena3= "Hola mundo \"esto esta en comillas\""
print("")
print("7. Cadenas entre comillas dobles: ")
print("")
print("Lexema: " + str(cadena3))
print("")
respuesta = re.search(' "[^"]*', str(cadena3))
print("")
print(respuesta)
print("")
if respuesta:
        print("Lexema: " + str(cadena3) + " Línea: " + str(respuesta.start()) + " Columna: " + str(respuesta.end()))
else:
    print("Lexema Invalido")