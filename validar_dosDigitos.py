#Escriba un programa que mediante una funcion valide a) que sea numero lo ingresado por teclado b)que maximo tenga solo dos digitos
#use los operadores try-catch para evitar el cierre del programa y solo se cierre cuando se ingresen dos digitos


def validarEntrada(numero):
    contador = 0
    while numero > 0:
        numero = numero//10
        contador +=1
    
    return contador
    



while True: 
    try:
        numero = int(input("Digita un numero: "))
        total_digitos = validarEntrada(numero)
        if total_digitos == 2:
            print("Entrada valida")
            break

    except ValueError:
        
        print("Valor no admitido")
