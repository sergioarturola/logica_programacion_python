"""
Usando compresion de listas eliminar elementos repetidos
"""

students = ["jamil", "tj", "abdullahi", "Jamil", "kabir", "rae", "abdulmujib", "Tj", "kabir"]
lower_students = [x.lower() for x in students]
new_students = [x for x in set(lower_students)]
print(new_students)
