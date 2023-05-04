#Dada una lista que cuyos elementos son diccionarios con nombres de estudiantes y sus #calificaciones, hacer un algoritmo que encuentre la nota mas baja donde 0 es las mas 
#baja y 100 la maxima
nombres = [
    {"juan" : 25},
    {"pedro" : 50},
    {"miguel" : 70},
    {"carlos" : 12},
    {"victor" : 66}
]

nota = 100


for elementos in nombres:
    for key, value in elementos.items():
        if nota > value :
            nota = value

print(nota)