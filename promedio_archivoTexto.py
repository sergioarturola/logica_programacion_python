#Escribe un programa que lea un archivo con las calificaciones de los estudiantes y muestre por pantalla
#unicamente las calificaciones y el promedio, las calificaciones seran extraidas de un archivo de texto

solo_numeros = []
file = open("promedio.txt", "r")
pasar_palabras = file.read().split()

for columnas in pasar_palabras:
    if columnas.isdigit():
        numero = int(columnas)
        solo_numeros.append(numero)


taman = len(solo_numeros)
suma =  sum(solo_numeros)
promedio = suma/taman

print("Las calificaciones de los alumnos son: ", solo_numeros)
print("El promedio es: ", promedio)