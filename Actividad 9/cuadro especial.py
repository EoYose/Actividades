#Crea una matriz nula de MxN
def matriz_nula(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz

def mostrar_matriz(matriz):
    for i in matriz:
        print(matriz)

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

def mover(pos, m, n):
    fila, columna = pos 
    columna += 1
    if columna > n:
        columna = 0
        fila += 1
    return (fila, columna) 

def valido(pos, candidato, candidato_max, tablero, aux,m,n):
    fila, columna = mover(pos,m,n)
    if not dentro_tablero((fila, columna),m,n):
        return False
    if movimiento_hecho((fila, columna), tablero):
        return False
    if candidato > candidato_max:
        return False
    if candidato <= aux[fila][columna]:
        return False
    return True

def tablero_completo(TABLERO, N):
    I = 0
    while I < N:
        J = 0
        while J < N:
            if TABLERO[I][J] == 0:
                    return 0
            J = J + 1
        I = I + 1
    return 1

def cuadrado_magico(TABLERO,N):
    AUX = SUMA_FILA(TABLERO,0, N)
    #AUX = 15
    I = 0
    while (I<N):
        if SUMA_FILA(TABLERO,I, N) != AUX:
            print(f"F{I}")
            return 0
        if SUMA_COLUMNA(TABLERO, I, N) != AUX:
            print(f"C{I}")
            return 0 
        I = I + 1
    if AUX != SUMA_DP(TABLERO, N):
        print("DP")
        return 0
    if AUX != SUMA_DS(TABLERO, N):
        print("DS")
        return 0

    return 1 # ES CUADRADO MAGICO

def SUMA_FILA(TABLERO, FILA, N):
    SUMA = 0
    for J in range(0,N):
        SUMA = SUMA + TABLERO[FILA][J]
    return SUMA

def SUMA_COLUMNA(TABLERO, COLUMNA, N):
    SUMA = 0
    for J in range(0,N):
        SUMA = SUMA + TABLERO[J][COLUMNA]
    return SUMA

def SUMA_DP(TABLERO, N):
    SUMA = 0
    for J in range(0,N):
        SUMA = SUMA + TABLERO[J][J]
    return SUMA

def SUMA_DS(TABLERO, N):
    SUMA = 0 ; J = N - 1
    I = 0
    while I < N:
        SUMA = SUMA + TABLERO[I][J]
        J = J - 1
        I = I + 1
    return SUMA


n = 3
m = n
tablero = matriz_nula(n,m)
aux = matriz_nula(n,m)
solucion_encontrada = False
solucion = False
candidato = 1
candidato_max = m*n
h_pos = [(0,0)]

while solucion_encontrada == False:
    if valido(h_pos[-1], candidato, candidato_max, tablero, aux, m, n):
        h_pos.append(h_pos[-1],m,n)
        x,y = h_pos[-1]
        tablero[x][y] = candidato
        if tablero_completo(tablero, n):
            if cuadrado_magico(tablero,n):
                solucion_encontrada = True
                solucion = True


