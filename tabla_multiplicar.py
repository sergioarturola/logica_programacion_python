#Realizar un programa que pida por teclado un numero y despliegue la tabla de multiplicar
#de dicho numero 

numero = int(input("Digita un numero: "))

for i in range(1, 11):
    print(numero , " x ",i," = ", numero * i)
