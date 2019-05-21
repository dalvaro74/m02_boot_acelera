def normal(x):
    return x

def sumaTodo(limitTo,f):
    resultado = 0
    for cont in range(1, limitTo+1):
        resultado += f(cont)
    return resultado
if __name__ == "__main__": 
    print(sumaTodo(100,normal))