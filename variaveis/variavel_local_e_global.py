def somalista(lista):
    global soma
    for item in  lista:
        if type(item) is list:
            somalista(item)
        else:
            soma +=item

soma = 0
somalista([[1,2],[3,4,5],6])

print(soma)