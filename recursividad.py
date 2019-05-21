def retrocontador(e):
    if e>0:
        print("{},".format(e),end="")
        retrocontador(e-1)
    else:
        print(0)
#LLega hasta 2.500 sin petar
retrocontador(10)

def sumatorio(n):
    if n>0:
        return n+sumatorio(n-1)
    else:
        return 0
    
print(sumatorio(4))

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
print(factorial(5))