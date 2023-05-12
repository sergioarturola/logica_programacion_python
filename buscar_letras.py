#Realizar un programa que permita ingresar por teclado una cadena de texto y posteriormente
#tambien en formato de texto pedir la o las letras que se desean encontar al final mostrar
#el indice y las letras en caso de que esten en la cadena

palabra = input("Escribe un texto: ")
letras = input("Ingresa la letra/s a buscar: ")
letra_buscar = [letra for letra in letras]
lista_letras = [letras for letras in palabra]

for index, letra in enumerate(lista_letras):
    for buscar in letra_buscar:
        if(buscar == letra):
            print(index, letra)
