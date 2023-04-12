#Escribe un programa que lea la frase y regrese los ultimos caracteres de cada palabra
#entrada = Esto es programacion divertida | salida = osna
#entrada = Todos somos responsables | salida = sss

def ultimosCaracteres(frase):
    lista = []
    pasar = frase.split()
    for letras in pasar:
        ultimo = letras[-1:] #con los [] sacamos un subtring, en este caso le decimos que queremos la ultima palabra
        lista.append(ultimo)

    ultimos_caracteres = " ".join(lista)
    return ultimos_caracteres




frase1 = "Esto es programacion divertida"
frase2 = "Todos somos responsables"
print(ultimosCaracteres(frase1))
print(ultimosCaracteres(frase2))




