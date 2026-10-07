def MATRIZ_NULA(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz

def CANDIDATO_ES_VALIDO(TABLERO, CANDIDATO, N):
	I = 0
	while I < N:
		J = 0
		while J < N:
			if TABLERO[I][J] == CANDIDATO:
				return 0
			J = J + 1
		I = I + 1
	return 1

def LLEGO_AL_FINAL(TABLERO, N):
	I = 0
	while I < N:
		J = 0
		while J < N:
			if TABLERO[I][J] == 0:
					return 0
			J = J + 1
		I = I + 1
	return 1

def SIGUIENTE_XY(TABLERO):
	I = 0
	while I < N:
		J = 0
		while J < N:
			if TABLERO[I][J] == 0:
					return (I, J)
			J = J + 1
		I = I + 1

def DEVOLVER(TABLERO, I, J, N):
	J = J - 1
	if J == -1 :
		I = I - 1
		J = N - 1
	return (I, J)

def MOSTRAR_MATRIZ(matriz):
	for i in matriz:
		print(i)

def CUADRADO_MAGICO(TABLERO,N):
	#AUX = SUMA_FILA(TABLERO,0, N)
	AUX = 15
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

X,Y = 0, 0
N = 3
CANDIDATO = 1; SOLUCION = False ; X_INICIAL = 0 ; Y_INICIAL = 0
TABLERO = MATRIZ_NULA(N,N)

while CANDIDATO <= N*N or SOLUCION == False:
	if CANDIDATO_ES_VALIDO(TABLERO, CANDIDATO, N):
		TABLERO[X][Y] = CANDIDATO
		if LLEGO_AL_FINAL(TABLERO, N):
			print("condicion final")
			MOSTRAR_MATRIZ(TABLERO)
			if CUADRADO_MAGICO(TABLERO, N):
				SOLUCION = True
			else:
				CANDIDATO = CANDIDATO + 1 ; TABLERO[X][Y] = 0
				while (X != X_INICIAL and Y != Y_INICIAL ) and (CANDIDATO == 10):
					X, Y = DEVOLVER(TABLERO, X, Y, N)
					CANDIDATO = TABLERO[X][Y] + 1
					TABLERO[X][Y] = 0
		else:
			X, Y = SIGUIENTE_XY(TABLERO)
			CANDIDATO = 1
	else:
		CANDIDATO = CANDIDATO + 1 
		while (X != X_INICIAL and Y != Y_INICIAL ) and (CANDIDATO == 10):	
			X, Y = DEVOLVER(TABLERO, X, Y, N)
			CANDIDATO = TABLERO[X][Y] + 1
			TABLERO[X][Y] = 0

MOSTRAR_MATRIZ(TABLERO)


		
	
