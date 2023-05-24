#Pedir al usuario 10 palabras y mostrarlas de la ultima a la primera

palabra = []

for i in range(10):
    cadena = input("Escribe palabra: ")
    palabra.append(cadena)


for i in range(10):
    print(palabra.pop())
print(palabra)
