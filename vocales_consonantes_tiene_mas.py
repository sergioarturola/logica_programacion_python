"""
Realizar un programa que permita una frase y muestre si tiene más vocales o más consonantes  
Ejemplo . De la frase  " mi perro se encuentra contemplando el cielo " 
el resultado mostrado sería : la frase cuentan con mas consonantes que vocales 
"""

consonantes = 0
vocales = 0
lista_vocales = ['a', 'e', 'i', 'o', 'u']

frase = input("Igresa una frase: ")

for letras in frase:
    if letras in lista_vocales:
        vocales +=1

    #para que no cuente caracteres como ?!.-+ ...etc
    if  letras.isalpha() and letras not in lista_vocales:
        consonantes += 1


#imprimiendo el mensaje
if vocales > consonantes:
    print("La frase tiene mas vocales que consonantes")
else:
    print("La frase tiene mas consonantes que vocales")
