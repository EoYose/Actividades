#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)
import copy
import os
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
	if J == -1:
		I = I - 1
		J = N - 1
	return (I, J)

def MOSTRAR_MATRIZ(matriz):
	for i in matriz:
		print(i)

def CUADRADO_MAGICO(TABLERO,N):
	AUX = SUMA_FILA(TABLERO,0, N)
	#AUX = round((N*(N**2+1))/2)
	#AUX = 15
	I = 0
	while (I<N):
		if SUMA_FILA(TABLERO,I, N) != AUX:
			#print(f"F{I}")
			return 0
		if SUMA_COLUMNA(TABLERO, I, N) != AUX:
			#print(f"C{I}")
			return 0 
		I = I + 1
	if AUX != SUMA_DP(TABLERO, N):
		#print("DP")
		return 0
	if AUX != SUMA_DS(TABLERO, N):
		#print("DS")
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

def guardar(file_name, info):
	if os.path.isfile(file_name):
		print("Archivo existente")
		print("sobre escribiendo archivo")
	else:
		print(f"Creando {file_name}")
	with open(file_name,"w+") as file:
		file.write(info)

def leer(nombre):
	if os.path.isfile(f"{nombre}.txt"):
		with open(f"{nombre}.txt","r") as file:
			referencia = file.read()
	else:
		with open(f"{nombre}.txt","+w") as file:
			referencia = " "
	return referencia

X,Y = 0, 0
N = 3
CANDIDATO = 1; SOLUCION = False ; X_INICIAL = 0 ; Y_INICIAL = 0
TABLERO = MATRIZ_NULA(N,N)
soluciones = []
registro = []

while CANDIDATO <= N*N and SOLUCION == False:
	if CANDIDATO_ES_VALIDO(TABLERO, CANDIDATO, N):
		TABLERO[X][Y] = CANDIDATO
		registro.append(copy.deepcopy(TABLERO))
		if len(registro) >= 50:
			registro.pop(0)
		#MOSTRAR_MATRIZ(TABLERO)
		#print("-"*10)
		if LLEGO_AL_FINAL(TABLERO, N):
			if CUADRADO_MAGICO(TABLERO, N):
				print("-"*20)
				soluciones.append(copy.deepcopy(TABLERO))
				#MOSTRAR_MATRIZ(TABLERO)
				#SOLUCION = True
			else:
				CANDIDATO = CANDIDATO + 1 ; TABLERO[X][Y] = 0
				while not (X == X_INICIAL and Y == Y_INICIAL) and (CANDIDATO == N*N+1):
					X, Y = DEVOLVER(TABLERO, X, Y, N)
					CANDIDATO = TABLERO[X][Y] + 1
					TABLERO[X][Y] = 0
		else:
			X, Y = SIGUIENTE_XY(TABLERO)
			CANDIDATO = 1
	else:
		CANDIDATO = CANDIDATO + 1 
		while not (X == X_INICIAL and Y == Y_INICIAL) and (CANDIDATO == N*N+1):	
			X, Y = DEVOLVER(TABLERO, X, Y, N)
			CANDIDATO = TABLERO[X][Y] + 1
			TABLERO[X][Y] = 0


#Mostrar resultados
TABLERO = soluciones[0]
print("#"*20)
print("Solucion")
print("Constante magica: "+str((N*(N**2+1))/2))
aux = 0
for i in range(0,len(TABLERO)):
	aux += TABLERO[0][i]
print("Constante actual: "+str(aux))
MOSTRAR_MATRIZ(TABLERO)
print("#"*20)

#revisar registros de N soluciones
referencia = leer("solucion").split("N")
n_registradas = []
for i in referencia:
	i = i.split("\n")[0]
	i = i.strip("=")
	if i.isnumeric():
		n_registradas.append(int(i))

if not N in n_registradas: #solucion no anotada
	with open("solucion.txt","a") as file:
		file.write("\n")
		file.write("N="+str(N))
		file.write("\n")
		for fila in soluciones[0]:
			file.write(str(fila).strip("[]"))
			file.write("\n")

#revisar registros de N soluciones
referencia = leer("Todas_las_soluciones").split("N")
n_registradas = []
for i in referencia:
	i = i.strip("=")
	if len(i) !=0:
		i=i[0]
	if i.isnumeric():
		n_registradas.append(int(i))

if not N in n_registradas: #solucion no anotada
	with open("Todas_las_soluciones.txt","a") as file:
		file.write("\n")
		file.write("N="+str(N))
		file.write("\n")
		for solucion in soluciones:
			for fila in solucion:
				file.write(str(fila).strip("[]"))
				file.write("\n")
			file.write("\n\n")

