"""
Solicitar numeros por consola, validar que unicamente sean enteros
-si se ingresa el numero 0 dejar de pedir numeros y mostrar la lista
no se debe de agregar el 0
-Preguntar si se desea eliminar un numero, si el numero se encuentra eliminarlo
y mostrar la lista actualizada sino mandar un mensaje

NOTA: Usar funciones, al menos 1 funcion lambda y 1 con operador ternario
"""
def manageList(lista):
    bandera = True

    while bandera:
        print(lista)
        respuesta = input("Eliminar elemento (e) || Salir (s)) || Volver a ingresar nuermos (v): ").lower()

        if((respuesta != "e") and (respuesta != "s") and (respuesta != "v")):
            print("--- Comando no reconocido, vuelve a intenarlo ---")


        if(respuesta == "s"):
            bandera = False


        if(respuesta == "e"):
            elemento = input("Ingresa elemento a eliminar: ")
            if elemento in lista:
                lista.remove(elemento)
            else:
                print("Elemento no encontrado")
        

        if(respuesta == "v"):
            print("+-- Si regresa se perdera los datos de la lista +--")
            regresar = input("Continuar? (y/n): ")
            if regresar == "y": 
                programa()
            


def validateNum(n):
    return n.isdigit() if True else False


def programa():

    li_numbers = list()
    bandera = True
    while bandera:
        number = input("Ingresa un numero: ")
        if(number == "0"):
            bandera = False


        if validateNum(number) and number != "0":
            li_numbers.append(number)

    manageList(li_numbers)
        

    
        

 #llamada a la funcion       
programa()




