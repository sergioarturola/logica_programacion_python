#ingresar un numero y decir si es:
#unidad -> 1 |decena ->10  |centena ->100 |milesima ->1000 |decena de mil ->10,000 |centena de mil->100,000

contador = 0
numero = int(input("Ingresa un numero: "))

while numero > 0:
    
    numero //=10
    contador = contador + 1
    
    
    
print("Numero de ", contador," cifras")

if contador == 1:
    print("Unidad")
elif contador == 2:
    print("Decena")
elif contador == 3:
    print("Centena")
elif contador == 4:
    print("Milesima")
elif contador == 5:
    print("Decena de mil")
elif contador == 6:
    print("Centena de mil")
else:
    print("Millon")
