#crea un programa que dadas dos cadenas de texto de la misma longitud intercale cada caracter y forme una nueva palabra
cadena1 = "hola caracola"
cadena2 = "adios marieta"
cad1 = list(cadena1) #pasamos las cadenas a listas
cad2 = list(cadena2)
lista = [] #lista vacia

#usando zip para generar una tupla por cada valor de las listas
for v1, v2 in zip(cad1, cad2):
    lista.append(v1)
    lista.append(v2)

nueva = "".join(lista) #juntando la palabra
print(nueva)



