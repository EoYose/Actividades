def obtener_candidatos(n):
    candidatos = []
    aux = []
    aux2 = [1 for _ in range(n)]
    magico = (n*(n**2+1))/2
    while True:
        for i in range(0, n):
            for j in range(aux2[i], n*n+1):
                if j not in aux:
                    aux.append(j)
                    break
        if not sum(aux) == magico:
            aux = []
            aux2[-1] += 1
            for i in range(1, n+1):
                if aux2[-i] > n*n:
                    aux2[-i] = 1
                    if i == n:
                        return candidatos
                    aux2[-(i+1)] += 1
        else:
            if len(aux) == n and aux not in candidatos:
                candidatos.append(aux.copy())

def agrupar_candidatos(candidatos, n):
    def agrupar(candidatos):
        grupo = []
        resto = []
        grupo.append(candidatos.pop(0))
        while len(candidatos) > 0:
            i = 0
            while i < len(candidatos):
                j = 0
                while j < len(candidatos[i]):
                    if sorted(candidatos[i]) == sorted(grupo[0]):
                        grupo.append(candidatos.pop(i))
                        break
                    j += 1
                i += 1
            resto.extend(candidatos[0:i])
            candidatos = candidatos[i:]
        return grupo, resto
    grupos = []
    while len(candidatos) > 0:
        grupo, resto = agrupar(candidatos)
        grupos.append(grupo)
        candidatos = resto
    return grupos

def mostrar_matriz(matriz):
    for i in matriz:
        print(str(i))

def mostrar_largo(matriz):
    for i in matriz:
        print(len(i))

a = agrupar_candidatos(obtener_candidatos(n), n)
#mostrar_matriz(a)
mostrar_largo(a)