def normal(x):
    return x

def sumaTodo(limitTo,f):
    resultado = 0
    for cont in range(1, limitTo+1):
        resultado += f(cont)
    return resultado

print(sumaTodo(100,normal))