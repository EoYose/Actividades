#Crea una matriz nula de MxN
def matriz_nula(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz

def dentro_tablero(pos,m,n):
    fila, columna = pos
    if not 0 <= fila < m:
        return False
    if not 0 <= columna < n:
        return False
    return True

#Consulta si la posicion ya fue hecha
def movimiento_hecho(pos,tablero):
    fila, columna = pos
    return tablero[fila][columna] != 0

def valido(candidato,m,n. aux):
    if not dentro_tablero(candidato,m,n):
        return False
    if movimiento_hecho(candidato, tablero):
        return False

n = 3
tablero = matriz_nula(n,n)
aux = matriz_nula(n,n)
solucion_encontrada = False
solucion = False
candidato = 1
historial_posiciones = []

while solucion_encontrada == False:
    if valido(candidato):
        pass