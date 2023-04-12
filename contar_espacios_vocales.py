#Escribir un programa que permita ingresar una cadena por teclado y al final muestre
#la cantidad de vocales y espaciones de la cadena

espacios = 0
vocales = ['a', 'e', 'i', 'o', 'u']
cuenta_vocal = 0

texto = input("Escribe algo: ")

for letras in texto:
    if letras == " ":
        espacios = espacios+1
    if letras in vocales:
        cuenta_vocal = cuenta_vocal + 1



print("total de espacios en blanco: ", espacios)
print("total de vocales: ", cuenta_vocal)
print(texto.upper())
