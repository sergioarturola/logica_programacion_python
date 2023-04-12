#En este ejercicio se realizara el clasico juego de piedra, papel o tijera donde por teclado se pregunta al
#jugador que desea escoger y la computadora usando la libreria random escoge una opcion, despues debe de indicar
#si el jugador perdio, empato o gano contra la computadora, usar funciones

import random

def jugar():
    usuario = input("Eligre una opcion...Pi->Piedra..Pa->Papel..Ti-> Tijera\n").lower() #para que todo se convierta en minuscula
    computadora = random.choice(["pi", "pa", "ti"])

    if usuario == computadora:
        return "Empate!!!"
    
    #retornando una funcion que regrese True o False comparando user y computer
    
    if gano_jugador(usuario, computadora): #funcion con argumentos (llamada a la funcion)
        return "Ganaste!!!"
    
    return "Perdiste!!!" #si no se cumple el empate o ganaste


def gano_jugador(jugador, oponente): #funcion con parametros (declarando la funcion)
    
    #Retorna True si gana Jugador y las formas de que gane son:
    # piedra gana tijera (pi>ti)
    #papel gana pidra (pa>pi)
    #tijera gana papel(ti>pa)
    
    if((jugador == "pi" and oponente == "ti")
        or (jugador == "pa" and oponente == "pi")
        or (jugador == "ti" and oponente == "pa")):
        return True
    else:
        return False



print(jugar())

