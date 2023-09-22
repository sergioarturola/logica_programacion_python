def suma(x, y):
    return x+y


def sumaArgs(*args):
    return sum(elemento for elemento in args)



print(sumaArgs(1,2,3))
print(sumaArgs(1,2,3,4,5,6,7))
