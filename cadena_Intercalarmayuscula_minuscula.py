#Dada una cadena de texto ingresada por teclado, imprimir
#la cadena alternando entre mayusculas y minusculas

cadena = input("Ingresa cadena: ")
intercalado = ""
contador = 0

for letras in cadena:
    if contador %2== 0:
        intercalado += letras.capitalize()
    else:
        intercalado +=letras.lower()
    
    contador += 1


print(intercalado)

