 


arreglo = [3,4,2,1]

def imprimir(texto="",i=0):
    n = len(texto)
    if i < n:
        imprimir(texto,i+1)
        print(texto[i])

imprimir("hola")    

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


#print(ordenar_iterativo(arreglo,len(arreglo)))