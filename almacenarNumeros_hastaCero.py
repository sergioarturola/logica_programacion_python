#pedir por teclado numeros, almacenarlos en una lista hasta que el usuario ponga cero, despues mostrar la lista en orden descendente

numeros = []
nocero = True

while nocero:
    numero = int(input("Digita un numero: "))
    if numero != 0:
        numeros.append(numero)
    else:
        break

numeros.sort(reverse=True)

print(numeros)
