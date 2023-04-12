#Realizar en python un programa que simule un juego de lanzamiento de una moneda, el programa debe de
#preguntar por teclado si el usuario elige cara o cruz, si coincide con el lanzamiento mandar el mensaje
#diciendo "Ganaste" en caso contrario "Perdiste"

import random

coin = ["cara", "cruz"]
lanzar = random.choice(coin)

adivinar = input("Escoge cara/cruz: ")
if adivinar == lanzar:
    print("Ganaste!!!")

else:
    print("perdiste :(" )
    if lanzar == "cara":
        print("Era cara!!")
    elif lanzar == "cruz":
        print("Era cruz!!")