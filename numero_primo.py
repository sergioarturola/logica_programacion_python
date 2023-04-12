#Escribir un programa que mediante una funcion determine si un
#numero es primo o no

def es_primo(num):
    i = 2
    while i <= num:
        if num % i == 0:
            return False
        
        
        i = i + 1
        return True 



print(es_primo(6))
print(es_primo(8))
print(es_primo(7))

