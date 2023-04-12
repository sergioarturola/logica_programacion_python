#Realiza un programa en Python con las siguientes caracteristicas:
#crea un juego donde la computadora genere un numero aleatorio pero
#donde el usuario puede elegir el rango superior e inferior, tambien
#debe de dar pistas al usuario si es numero es demasiado alto o demasiado
#bajo, el programa termina cuando el usuario adivina el numero
#Usar funciones

import random

def ingresarRango():
    inferior = int(input("Ingresa rango inferior: "))
    superior = int(input("Ingresa rango superior: "))

    aleatorio_compu = random.randint(inferior, superior)
    return aleatorio_compu


def pregunta():
    usuario = int(input("Estoy pensando en un numero, adivina! : "))
    return usuario


def verificar(usuario, aleatorio):
    sigue_intentando = True
    
    while sigue_intentando:
        
        if aleatorio == usuario:
            print("Felicidades!! ganaste")
            sigue_intentando = False
        
        elif usuario > aleatorio:
            usuario = int(input("Demsaiado alto, vuele a intentarlo:" ))
        else:
            usuario = int(input("Demasiado bajo, vuelve a intentarlo: "))


def main():
    num_alazar = ingresarRango()
    print(num_alazar)
    num_user = pregunta()
    verificar(num_user, num_alazar)

    
main()

