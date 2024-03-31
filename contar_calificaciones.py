"""
Escribe una funcion llamada "grade_stats" que reciba una lista como parametro y devuelve
un diccionario que mapea cuantas veces aparecieron las calificaciones, maneje errores
en caso de que no se pase una lista como argumento
"""

def grade_stats(grades: list) -> dict:
    gradeDict = dict()

    if( type(grades) != list or grades == []):
        return gradeDict
    
    for grade in grades:
        if grade in gradeDict:
            gradeDict[grade] += 1
        else:
            gradeDict[grade] = 1

    return gradeDict


print(grade_stats(["A","A", "E", "B", "B", "D", "C"]))
print(grade_stats([10, 8, 7, 7, 8, 9, 8]))
print(grade_stats("hola"))
print([])
