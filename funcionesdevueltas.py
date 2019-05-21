def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for valor in l:
        if valor > m:
            m = valor            
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for valor in l:
        if valor < m:
            m = valor           
    return m

def media(*l):
    if len(l) == 0:
        return 0
    media = 0
    for valor in l:
        media += valor    
    return media/len(l)

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
    }

def returnF(nombreFuncion):
    nombre = nombreFuncion.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    else:
        return None
