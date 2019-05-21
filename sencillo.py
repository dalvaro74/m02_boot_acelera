def sumaTodo(limitTo):
    resultado = 0
    for cont in range(1, limitTo+1):
        resultado +=cont
    return resultado

print(sumaTodo(100))