#Se pide que con 3 funciones, una con pedir_nombre se ingrese a la cadena pero no permitir que se ingrese vacia
#otra llamada es_nombre_py que verifica si el texto ingresado antes del punto contiene texto, y despues del punto
#tiene terminacion py

def pedir_nombre():
    
    while True:

        nombre = input("Escribe el nombre del archivo: ")
        
        if len(nombre) == 0:
            print("Campo no puede quedar vacio")
            continue
        
        else:
            return nombre
            break
            
    
   
def es_nombre_py():

    
    
    while True:

        nombre = pedir_nombre()
        empiezo = nombre[:nombre.index(".")]
        termino = nombre[nombre.index(".")+1:]
        indice = nombre[0]

        if not empiezo or "py" not in termino:
            print("archivo o formato no valido")
            continue
            #pedir_nombre()
            
    
            
    
    
        else:
    
            if indice.isdigit():
                print("No debe ser digito el primer caracter")
                continue
                #pedir_nombre()
            
        
                
    
            else:
                print("El archivo esta ok")
                print("Nombre: " +empiezo)
                print("Terminacion: " +termino)
                break

    

def main():
    
    print("Porfavor escribe solo un archivo python")
    es_nombre_py()


main()