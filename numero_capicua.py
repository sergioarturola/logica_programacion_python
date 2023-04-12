#Escribir un programa en python que verifique si un numero es capicua o no

numero = input("Escribe un numero: ")
numero_reversa = numero[::-1]
print(numero_reversa)
if numero == numero_reversa:
    print("Es un numero capicua!!")
else:
    print("NO es un numero capicua")