#Escribir un algoritmo en el cual se introduzca un numero y se verifique si es multiplo de 4 o no

numero = int(input("Escribe un numero"))

if numero  % 4 == 0:
    print(f"El numero {numero} es multiplo de 4")
else:
    print(f"El numero {numero} NO es multiplo de 4")