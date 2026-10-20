 
arreglo = [3,4,2,1]

def imprimir(texto="",i=0):
    n = len(texto)
    if i < n:
        imprimir(texto,i+1)
        print(texto[i])

#imprimir("hola")    

def ordenar_arreglo(arreglo,i):
    n = len(arreglo)
    if arreglo[i] >= arreglo[i+1]:
        aux = arreglo[i+1]
        arreglo[i+1] = arreglo[i]
        arreglo[i] = aux
    else:
        if n > i:
            return ordenar_arreglo(arreglo,i+1)
        return arreglo

def ordenar_iterativo(arreglo,n):
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                swapped = True
        if not swapped: break
    return arreglo

def ordenar_iterativo3(arreglo):
    n = len(arreglo)
    i = 0
    while i < n:
        swapped = False
        j = 0
        while j+1 < n-1:
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                swapped = True
        if not swapped: break
    return arreglo

def aux(arreglo,i,j):
    n = len(arreglo)
    swapped = False
    if arreglo[j] > arreglo[j+1]:
        arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        swapped = True
    if j < n-2-i:
        return aux(arreglo,i,j+1)
    return arreglo, swapped

def aux2(arreglo, i, swapped):
    n = len(arreglo)
    if i<n and swapped:
        arreglo, swapped = aux(arreglo,i,0)
    if i<n and swapped:
        return aux2(arreglo,i+1,swapped)
    return arreglo, i, swapped

print(aux2(arreglo,0,True)[0])

def ordenar_iterativo2(arreglo):
    n = len(arreglo)
    i = 0
    swapped = True
    while i < n and swapped:
        arreglo, swapped = aux(arreglo,i,0)
        i +=1
    return arreglo

def ordenar_recursivo(arreglo,i,j):
    n = len(arreglo)
    if i > n:
        return arreglo, False
    swapped = False
    if j < (n-1-i):
        arreglo, swapped = ordenar_recursivo(arreglo,i+1,j+1)
    if not swapped:
        return arreglo, swapped
    if arreglo[j] > arreglo[j+1]:
        arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        swapped = True
    return arreglo, swapped
    
#print(ordenar_recursivo(arreglo,0,0))

#print(ordenar_iterativo(arreglo,len(arreglo)))
#print(ordenar_iterativo2(arreglo))