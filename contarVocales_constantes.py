#Realizar un programa que cuente si una frase tiene mas vocales o constantes
#Ejemplo. De la frase “Mi perro se encuentra contemplando el cielo” el resultado 
#mostrado seria: La frase cuenta con más consonantes que vocales

vocales = ["a", "e", "i", "o", "u"]
letra_vocal = 0
letra_constante = 0
espacios = 0

frase = input("Escribe una frase: ").lower()

for letras in frase:
    if letras in vocales:
        letra_vocal +=1
    
    if letras.isspace():
        espacios +=1
    
    if letras not in vocales:
        letra_constante +=1


if letra_constante > letra_vocal:
    print("La frase tiene mas vocales que constantes")
else:
    print("La frase tiene mas constantes que vocales")

print("Se encontraron ",espacios)
print("Vocales:", letra_vocal)
print("Constantes: ",letra_constante)