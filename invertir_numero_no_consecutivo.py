#Pedir por teclado un numero, pero este tiene que cumplir ciertas condiciones 1- que sea un numero entero positivo 2-que no sea un numero consecutivo
#como 11, 22, etc y que tampoco sea numero capicua el programa no sebe de avanzar hasta que no se cumplan estas condiciones, considere las funciones 
#necesarias para realizar el programa y tambien manejo de excepciones en caso de que se ingrese algo diferente a un numero
#
def invertir(numero):
    
    reverso = 0
    while numero >0:
        resto = numero % 10
        reverso = reverso * 10 + resto
        numero = numero // 10
    return reverso


def numeroConsecutivo(numero):
    verificando = str(numero)
    if(verificando[0] == verificando[1] or verificando == verificando[::-1]):

        return False
    else:
        return True



bandera = True

while bandera:

    ingreso = input("Ingresa un numero: ")
    try:
        numero = int(ingreso)
        if (isinstance(numero, int)):
            print("El numero invertido es: ", invertir(numero))
            print("Correcto")
            bandera = False
        
    except ValueError:
        print("Ingresa solo numeros enteros positivos")

  
print("Fin del programa")