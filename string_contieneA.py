#Realizar un script donde se ingrese una nombre y verificar si contiene la letra "a"
#si es asi entonces mandar un mensaje de Bienvenida + nombre, si no es asi decier que
#es un nombre invalido 

def validar(usuario):
    if 'a' in usuario:
        return True
    else:
        return False


usuario = input("Escribe un nombre, debe tener una a: ")
if validar(usuario):
    print(f"Bienvenido {usuario}")
else:
    print("Nombre invalido")