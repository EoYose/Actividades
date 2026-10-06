def matriz_nula(m:int,n:int):
	matriz = []
	for fila in range(m):
		aux = []
		for columna in range(n):
			aux.append(0)
		matriz.append(aux)
	return matriz #[[0]*n for _ in range(m)]

def marcar_tablero_reinas(pos, tablero, m,n):
	x,y = pos #Fila, columna
	for i in range(m):
		if 1 != i:
			tablero[i][y] = -1			
	for j in range(n):
		if 1 != j:
			tablero[x][j] = -1
	return tablero

def mostrar_tablero(tablero):
	for i in tablero:
		print(i)

def mover_reina(pos, direccion, magnitud):
	f,c = pos
	match direccion:
		case 1:
			#arriba
			f -= magnitud
		case 2:
			#arriba-derecha
			f -= magnitud
			c += magnitud
		case 3:
			#derecha
			c += magnitud
		case 4:
			#derecha abajo
			f += magnitud
			c += magnitud
		case 5:
			#abajo
			f += magnitud
		case 6:
			#abajo izquierda
			f += magnitud
			c -= magnitud
		case 7:
			#izquierda
			c -= magnitud
		case 8:
			#izquierda arriba
			f -= magnitud
			c -= magnitud
	return (f,c)

#Consulta si la posicion esta dentro del tablero
def dentro_tablero(pos,m,n):
	fila, columna = pos
	if not 0 <= fila < m:
		return False
	if not 0 <= columna < n:
		return False
	return True

def probar_colision(pos, reinas, m,n):
	for reina in reinas:
		for direccion in range(1,9):
			for magnitud in range(-m*n,m*n):
				mpos = mover_reina(reina, direccion, magnitud)
				if dentro_tablero(reina,m,n) == False:
					break
				if mpos == pos:
					return True
	return False



m,n = 7,8
x,y = 3,4
tablero = matriz_nula(m,n)
print(probar_colision((x,y),[(5,8)],m,n))
