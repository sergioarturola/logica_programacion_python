#Escribe un algoritmo usando python donde se detecte si hay caracteres consecutivos
#por ejemplo la palabra muestra "alggo" tiene 2 "g" consecutivas

texto = "alggo"

for letra, letra_siguiente in zip(texto, texto[1:]):
    print(letra, letra_siguiente)