#Hacer un programa que pida el nombre y apellido y por consola muestre
# primero el apellido luego una coma y finalmente el nombre por ejemplo
# Juan Perez debe de devolver Perez, Juan

nombre_apellido = []
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_apellido.append(apellido)
nombre_apellido.append(nombre)
resultado = ",".join(nombre_apellido)

print(resultado)
