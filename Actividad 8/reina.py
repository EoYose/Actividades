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
	if aux[c] > f:
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
	return paso == n 

def preguntar_numero(text):
	while True:
		respuesta = input(text)
		if respuesta.isnumeric():
			numero = int(respuesta)
			return numero
		else:
			print("Por favor ingrese un numero")

def preguntar_opciones(opciones):
	for n in range(1,len(opciones)+1):
		print(f"{n}.{opciones[n-1]}")
	while True:
		respuesta = preguntar_numero(f"1-{len(opciones)+1}> ")
		if respuesta in range(1,len(opciones)+1):
			return respuesta
		else:
			print("Opcion fuera de rango")

def devolver(historial_posiciones, tablero, paso, aux, candidato_x):
	f, c = historial_posiciones.pop() ; tablero[f][c] = 0
	paso -= 1
	candidato_x = aux[paso-1] + 1
	aux[paso] = -1
	return historial_posiciones, tablero, paso, aux, candidato_x

def poner_reinas(historial_posiciones, tablero, n, aux, paso, candidato_x):
	solucion = False
	while True:
		pos = (candidato_x, paso-1) # (fila, columna)
		
		#Movimiento valido?
		if validar(pos, historial_posiciones, aux, n,n):
			f,c = pos ; tablero[f][c] = paso
			historial_posiciones.append(pos)
			if final(paso,n):
				solucion = True;break
			else:
				aux[paso-1] = candidato_x ; candidato_x = 0 ; paso += 1

		else:
			#Intentar con el siguiente movimiento
			candidato_x += 1
			while len(historial_posiciones) > 0 and candidato_x > n:
				historial_posiciones, tablero, paso, aux, candidato_x = devolver(historial_posiciones,
				tablero, paso, aux, candidato_x)

			#Fin por agotamiento
			if len(historial_posiciones) == 0 and candidato_x >= n+1:
				solucion = False;break
	return solucion, historial_posiciones, tablero, aux, paso, candidato_x

print("Defina el tamaño N del tablero")
n = preguntar_numero("NxN: ")

#Inicializacion
tablero = matriz_nula(n,n)
aux = [-1 for _ in range(0,n,1)] #se usa -1 en vez de 0 ya que 0 ahora representa fila 0
paso = 1
candidato_x = 0
historial_posiciones = []
solucion = True
soluciones = []

while solucion == True:
	solucion, historial_posiciones, tablero, aux, paso, candidato_x = poner_reinas(historial_posiciones,
	tablero, n, aux, paso, candidato_x)
	if solucion == True:
		soluciones.append(copy.deepcopy(tablero))
		mostrar_tablero(tablero)
		print("#"*20)
		f, c = historial_posiciones.pop()
		tablero[f][c] = 0
		candidato_x = f + 1
		aux[c] = f
		paso = c + 1


del solucion

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



referencia = leer("solucion").split("N")
n_registradas = []
for i in referencia:
	i = i.split("\n")[0]
	i = i.strip("=")
	if i.isnumeric():
		n_registradas.append(int(i))

if not n in n_registradas: #solucion no anotada
	with open("solucion.txt","a") as file:
		file.write("\n")
		file.write("N="+str(n))
		file.write("\n")
		for fila in soluciones[0]:
			file.write(str(fila).strip("[]"))
			file.write("\n")

del referencia
del n_registradas
referencia = leer("Todas_las_soluciones").split("N")
n_registradas = []
for i in referencia:
	i = i.strip("=")
	if len(i) !=0:
		i=i[0]
	if i.isnumeric():
		n_registradas.append(int(i))

if not n in n_registradas:
	with open("Todas_las_soluciones.txt","a") as file:
		file.write("\n")
		file.write("N="+str(n))
		file.write("\n")
		for solucion in soluciones:
			for fila in solucion:
				file.write(str(fila).strip("[]"))
				file.write("\n")
			file.write("\n\n")



