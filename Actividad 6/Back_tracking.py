#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)

#Devuelve las coordenadas correspondientes al destino
def mover(pos, direccion):
    fila, columna = pos
    match direccion:
        case 1:
            fila -= 2
            columna += 1
        case 2:
            fila -= 1
            columna += 2
        case 3:
            fila += 1
            columna += 2
        case 4:
            fila += 2
            columna += 1
        case 5:
            fila += 2
            columna -= 1
        case 6:
            columna -= 2
            fila += 1
        case 7:
            columna -= 2
            fila -= 1
        case 8:
            fila -= 2
            columna -= 1
    return (fila, columna)

#Consulta si la posicion ya fue hecha
def movimiento_hecho(pos,tablero):
    fila, columna = pos
    return tablero[fila][columna] != 0

#Consulta si la posicion esta dentro del tablero
def dentro_tablero(pos,m,n):
    fila, columna = pos
    if not 0 <= fila < m:
        return False
    if not 0 <= columna < n:
        return False
    return True

#Obtiene las dimensiones del tablero
def obtener_dimensiones(matriz:list):
    m = len(matriz)
    n = []
    for fila in matriz:
        if any(isinstance(x, int) for x in fila):
            n.append(len(fila))
        else:
            raise ValueError(f"Formato Invalido, solo numeros. {fila}")
    if len(n) == n.count(n[0]):
        n = n[0]
        return m,n
    else:
        raise ValueError(f"Matriz con dimensiones irregulares, matriz con {m} filas y {n} columnas")

#Filtra los movimientos disponibles
def movimientos_disponibles(pos,tablero):
    disponibles = []
    m,n = obtener_dimensiones(tablero)
    for combinacion in range(1,9):
        intento = mover(pos,combinacion)
        if not dentro_tablero(intento,m,n):
            continue
        if movimiento_hecho(intento, tablero):
            continue
        disponibles.append(combinacion)
    return disponibles

#Verifica la condicion de termino del programa
#Tambien determina si el problema tiene solucion o no
def fin(dimensiones,conteo, historial_posiciones):
    m,n = dimensiones
    if m*n == conteo:
        return True
    else:
        if len(historial_posiciones) == 0:
            return False
    return None

#Crea una matriz nula de MxN
def matriz_nula(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz

m,n = (6,6)
tablero = matriz_nula(m,n)
tablero[0][0] = 1
aux = matriz_nula(m,n)

solucion = None
conteo = 1
candidato = 1
historial_posiciones = [(0,0)]
print("Buscando solucion")
while solucion == None:
    #Da los movimientos disponibles
    disponibles = movimientos_disponibles(historial_posiciones[-1], tablero)

    f, c = historial_posiciones[-1] #fila, columna
    #Movimiento valido?
    if candidato in disponibles and 8 >= candidato > aux[f][c]:
        conteo += 1

        #Anotar movimiento en aux
        fil, col = historial_posiciones[-1] #fila, columna
        aux[fil][col] = candidato

        #Oficializar movimiento 
        historial_posiciones.append(mover(historial_posiciones[-1], candidato))
        fil, col = historial_posiciones[-1] #fila, columna
        tablero[fil][col] = conteo
        
        candidato = 1

    else:
        #Intentar con el siguiente movimiento
        candidato += 1

    #Sin movimientos?
    if candidato > 8:
        candidato = 1 

        #Deshacer movimiento
        conteo -= 1
        f,c = historial_posiciones[-1]
        tablero[f][c] = 0
        aux[f][c] = 0
        del historial_posiciones[-1]

    solucion = fin((m,n), conteo, historial_posiciones)

#Muestra el tablero final
#print(f"\n".join([str(i) for i in tablero])) # Muestra solo el tablero
print(f"\n".join([str([str(i) for i in tablero][x]) + str([str(e) for e in aux][x]) for x in range(m)])) # Muestra el tablero y el tablero auxiliar
print("La existencia de la solucion es:", solucion)