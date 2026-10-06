#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)
import copy
import os

#Consulta si la posicion esta dentro del tablero
def dentro_tablero(pos,m,n):
	fila, columna = pos
	if not 0 <= fila < m:
		return False
	if not 0 <= columna < n:
		return False
	return True

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

#Filtra los movimientos disponibles
def validar(pos, reinas, m,n):
	if not dentro_tablero(pos,m,n):
		return False
	for reina in reinas:
		for direccion in range(1,9):
			for magnitud in range(-m*n,m*n):
				mpos = mover_reina(reina, direccion, magnitud)
				if dentro_tablero(reina,m,n) == False:
					continue
				if mpos == pos:
					return False
	return True

#Crea una matriz nula de MxN
def matriz_nula(m,n):
	matriz = []
	for fila in range(m):
		aux = []
		for columna in range(n):
			aux.append(0)
		matriz.append(aux)
	return matriz

#mostrar tablero
def mostrar_tablero(tablero):
	for i in tablero:
		print(i)

#Inicializacion
m,n = 10,10
tablero = matriz_nula(m,n)
candidato_max = 8
paso = 1
candidato_x = 0
candidato_y = 0
historial_posiciones = []

print("Buscando solucion")

while True:
	#Da los movimientos disponibles
	pos = (candidato_x, candidato_y)
	
	#Movimiento valido?
	if validar(pos, historial_posiciones,m,n):
		f,c = pos
		tablero[f][c] = paso
		paso += 1
		historial_posiciones.append(pos)
		
		candidato_x = 0
		candidato_y = 0

	else:
		#Intentar con el siguiente movimiento
		candidato_x += 1

	if candidato_x > m:
		candidato_x = 0
		candidato_y += 1

	#Sin movimientos?
	if candidato_y >= n:
		print("llegado a fin")
		print(f"se han puesto {paso-1} reinas")
		mostrar_tablero(tablero)
		break
