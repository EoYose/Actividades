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

#Detecta si las reinas pueden alcanzar la posicion
def colision_reinas(pos, reinas, m,n):
	for reina in reinas:
		for direccion in range(1,9):
			for magnitud in range(-m*n,m*n):
				mpos = mover_reina(reina, direccion, magnitud)
				if dentro_tablero(reina,m,n) == False:
					continue
				if mpos == pos:
					return True
	return False

#Filtra los movimientos disponibles
def validar(pos, reinas, aux, m,n):
	if not dentro_tablero(pos,m,n):
		return False
	if colision_reinas(pos, reinas, m,n):
		return False
	f,c = pos
	if aux[c] >= f:
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

def final(paso,n):
	print("paso", paso)
	return paso == n 

#Inicializacion
n = 4
tablero = matriz_nula(n,n)
aux = [-1 for _ in range(0,n,1)] #se usa -1 en vez de 0 ya que 0 ahora representa fila 0
paso = 1
candidato_x = 0
candidato_y = 0
historial_posiciones = []
solucion = False

print("Buscando solucion")

while True:
	#Da los movimientos disponibles
	#==Importante==
	# X representa fila
	# Y representa columna
	pos = (candidato_x, paso-1)
	
	#Movimiento valido?
	if validar(pos, historial_posiciones, aux, n,n):
		f,c = pos
		tablero[f][c] = paso
		historial_posiciones.append(pos)
		print("#"*10);mostrar_tablero(tablero)
		if final(paso,n):
			solucion = True
			break
		else:
			aux[paso-1] = candidato_x
			candidato_x = 0
			paso += 1
			print("aux", aux)

	else:
		#Intentar con el siguiente movimiento
		candidato_x += 1
		print("siguiente fila", candidato_x)
		while len(historial_posiciones) > 0 and candidato_x == n+1:
			f, c = historial_posiciones[-1]
			tablero[f][c] = 0
			del historial_posiciones[-1]
			paso -= 1
			candidato_x = aux[paso-1]
			aux[paso-1] = -1
			#Si se retorcede y revisa otra opcion, debe olvidar la rama de la cual retrocedio sin olvidar que ya paso por esa rama
			print("retroceder", candidato_x); print("nuevo aux", aux)

	#if candidato_x > n:
	#	candidato_x = 0
	#	candidato_y += 1

	#Sin movimientos?
	#if candidato_y >= n:
	#	print("llegado a fin")
	#	print(f"se han puesto {paso-1} reinas para un tablero de {n}x{n}")
	#	mostrar_tablero(tablero)
	#	break

print("llegado a fin")
print(f"se han puesto {paso-1} reinas para un tablero de {n}x{n}")
mostrar_tablero(tablero)

