#EScribe un programa que reciba con un ciclo "for" 4 puntajes (en forma de string) y en caso de que el usuario no ponga ningun puntaje
#ponga por defecto un cero en la lista, mostrar la lista con los puntajes

lista_puntajes = []

for i in range(4):
    puntajes = input("Escribe el puntaje: ")
    if puntajes == "":
        lista_puntajes.append("0")
    else:
        lista_puntajes.append(puntajes)

print(lista_puntajes)


