"""
Crear un programa que pida la cantidad de hombres y mujeres de un grupo y 
calcule el porcentaje 
"""

cantidad_hombres = int(input("Ingresa la cantidad de varones: "))
cantidad_mujeres = int(input("Ingresa la cantidad de mujeres: "))

total_grupo = cantidad_hombres + cantidad_mujeres

porcentaje_hombres = (cantidad_hombres/total_grupo)*100
porcentaje_mujeres = (cantidad_mujeres/total_grupo)*100

print(f"Hombres {porcentaje_hombres} %")
print(f"Mujeres {porcentaje_mujeres} %")
