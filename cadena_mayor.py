#Escribir un programa que pida 2 cadenas al usuario y luego determine si
#son iguales, si la primera es mas grande o la segunda es mas grande

cad1 = input("Escribe una frase: ")
cad2 = input("Escribe otra frase: ")

if cad1 == cad2:
    print("Las 2 cadenas son iguales")

elif cad1 > cad2:
    print("Cadena 1 es mayor que Cadena 2")

elif cad1 < cad2:
    print("Cadena 2 es mayor que Cadena 1")
