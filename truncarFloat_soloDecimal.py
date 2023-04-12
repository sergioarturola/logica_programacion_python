#Diseñe un programa que por teclado reciba un numero de coma flotante e imprima por pantalla
#solo la parte decimal entrada = 4.5 salida = 0.5 | entrada = -1.19 salida = .19

import math

numero = abs(float(input("Ingresa un numero: ")))

num_decimal, num_entero = math.modf(numero)

print("Parte decimal: {:.2f}".format(num_decimal))