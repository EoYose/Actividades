def matriz_con(m, n):
    a = elemento
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(a)
        matriz.append(aux)
    return matriz

a = matriz_con(3,3,[])
a[0][0].append(2)
print(a)