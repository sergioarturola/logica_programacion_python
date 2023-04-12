def palindromo_es(palabra):

    palabra = palabra.lower()
    return palabra == palabra[::-1]

print(palindromo_es("radar"))
print(palindromo_es("pigsito"))
