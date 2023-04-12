#Implementa una funcion llamada invertir() que reciba como parametro una cadena de texto y regrese la cadena con las palabras invertidas


def invertir(cadena):
    separar = cadena.split()
    separar.reverse()
    nueva = " ".join(separar)
    
    return nueva


frase1 = "todos me la pelan"
frase2 = "El respeto al derecho ajeno es la paz"
print(invertir(frase1))
print(invertir(frase2))