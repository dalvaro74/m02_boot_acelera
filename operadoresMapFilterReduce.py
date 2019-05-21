from functools import reduce 

lista = [1, 2, 3, 4]

listaDobles = map(lambda x:x*2, lista)

listaPares = filter(lambda x:x%2==0, lista)

sumatorio = reduce(lambda x,y:x+y, lista)

sumatorioDobles = reduce(lambda x,y:x+y*2, lista)

print(list(listaDobles))
print(list(listaPares))
print(sumatorio)
print(sumatorioDobles)