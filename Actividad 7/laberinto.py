#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)
import copy
import os

#Devuelve las coordenadas correspondientes al destino
def mover(pos, direccion):
	fila, columna = pos
	match direccion:
		case 1:
			fila -= 1
		case 2:
			columna += 1
		case 3:
			fila += 1
		case 4:
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

#Filtra los movimientos disponibles
def movimientos_disponibles(pos,MxN,tablero):
	disponibles = []
	m,n = MxN#obtener_dimensiones(tablero)
	for combinacion in range(1,5):
		intento = mover(pos,combinacion)
		if not dentro_tablero(intento,m,n):
			continue
		if movimiento_hecho(intento, tablero):
			continue
		disponibles.append(combinacion)
	return disponibles

#Verifica la condicion de termino del programa
#Tambien determina si el problema tiene solucion o no
def fin(salida, tablero):
	f,c=salida
	if len(historial_posiciones) == 0:
		return True, False
	elif tablero[f-1][c-1] > 0:
		return True, True
	else:
		return False, False

#Crea una matriz nula de MxN
def matriz_nula(m,n):
	matriz = []
	for fila in range(m):
		aux = []
		for columna in range(n):
			aux.append(0)
		matriz.append(aux)
	return matriz

def preguntar_numero(text):
	while True:
		respuesta = input(text)
		if respuesta.isnumeric():
			numero = int(respuesta)
			return numero
		else:
			print("Por favor ingrese un numero")

def retroceder(paso, historial_posiciones, tablero, aux):
	#Reiniciar candidato
	candidato = 1 

	#Deshacer movimiento
	paso -= 1
	f,c = historial_posiciones[-1]
	del historial_posiciones[-1]
	tablero[f][c] = 0
	aux[f][c] = 0
	return candidato, paso, historial_posiciones, tablero, aux

def predefinir_laberinto(file_name):
	file = open(file_name, "w+")
	default = """
#dimensiones
m = 4 #filas
n = 6 #columnas
#condiciones
inicio = (0,0)
salida = (4,6)
#obstaculos
#obstaculo valido desde (1,1) hasta (m,n)
obstaculo = (1,3)
obstaculo = (2,3)
obstaculo = (3,3)
obstaculo = (3,5)
obstaculo = (4,5)
	"""
	file.write(default)
	file.close()

def interptetar_archivo(file_name):
	def lista_normal(valor):
		valor = valor.replace("(","").replace(")","").replace("[","").replace("]","")
		valor = valor.split(",")
		return valor

	obstaculos = []

	file = open(file_name,"r")
	lectura = file.read().split("\n")
	file.close()
	lineas = []

	for i in range(len(lectura)):
		lectura[i] = lectura[i].strip().lower()
		if not (not "=" in lectura[i] or len(lectura[i]) == 0 or lectura[i].startswith("#")):
			lineas.append(lectura[i].split("#")[0])

	for linea in lineas:
		variable, valor = linea.split("=")
		variable = variable.strip()
		valor = valor.strip()
		if variable in ["fila","filas","m"]:
			m = int(valor)
		if variable in ["colimna", "columnas", "n"]:
			n = int(valor)
		if variable in ["tamaño","dimensiones"]:
			valor = lista_normal(valor)
			m = int(valor[0])
			n = int(valor[1])
		if variable == "inicio":
			valor = lista_normal(valor)
			inicio = (int(valor[0]), int(valor[1]))
		if variable in ["fin", "final", "salida"]:
			valor = lista_normal(valor)
			salida = (int(valor[0]), int(valor[1]))
		if variable == "obstaculo":
			valor = lista_normal(valor)
			obstaculo = (int(valor[0]), int(valor[1]))
			obstaculos.append(obstaculo)

	return m, n, inicio, salida, obstaculos

def cargar_laberinto():
	file_name = "laberinto.dat"
	if os.path.isfile(file_name):
		m,n,inicio,salida,obstaculos = interptetar_archivo(file_name)
	else:
		print("laberinto.dat no encontrado")
		print("Creando uno predeterminado")
		print("nota: el predeterminado contiene instrucciones de como modificarse")
		predefinir_laberinto(file_name)
		m,n,inicio,salida,obstaculos = interptetar_archivo(file_name)
	tablero = matriz_nula(m,n)
	aux = matriz_nula(m,n)
	x,y = inicio
	tablero[x][y] = 1
	del x,y
	salida = salida
	for obstaculo in obstaculos:
		x,y = obstaculo
		tablero[x-1][y-1] = -1
	historial_posiciones = [inicio]
	return m, n, tablero, aux, salida, historial_posiciones

def guardar(file_name, info):
	if os.path.isfile(file_name):
		print("Archivo existente")
		print("sobre escribiendo archivo")
	else:
		print(f"Creando {file_name}")
	with open(file_name,"w+") as file:
		file.write(info)

#Inicializacion del laberinto
m, n, tablero, aux, salida, historial_posiciones = cargar_laberinto()

#Inicializacion del sistema de backtracking
candidato_max = 4
solucion = False
solucion_encontrada = False
paso = 1
candidato = 1

#Inicializacion del modo de busqueda
lista_soluciones = []
mejor_tiempo = m*n + 1 #Facilita la escritura de la primera solucion
mejor_tablero = []

#Preguntar modo de busqueda
print("Elija modo de busqueda")
print("1.primer solucion")
print("2.Todos las soluciones (se guardara en un archivo)")
print("3.Buscar la mejor solucion")
while True:
	modo_busqueda = preguntar_numero("Opcion: ")
	if modo_busqueda in [1,2,3]:
		break
	else:
		print("opcion fuera de rango")
modo_busqueda = ["primer", "todas", "mejor"][modo_busqueda-1]

print("Buscando solucion")

while True:
	#Da los movimientos disponibles
	disponibles = movimientos_disponibles(historial_posiciones[-1], (m,n), tablero)

	f, c = historial_posiciones[-1] #fila, columna
	#Movimiento valido?
	if candidato in disponibles and candidato_max >= candidato > aux[f][c]:
		paso += 1
		#Anotar movimiento en aux
		fil, col = historial_posiciones[-1] #fila, columna
		aux[fil][col] = candidato

		#Oficializar movimiento 
		historial_posiciones.append(mover(historial_posiciones[-1], candidato))
		fil, col = historial_posiciones[-1] #fila, columna
		tablero[fil][col] = paso

		candidato = 1


	else:
		#Intentar con el siguiente movimiento
		candidato += 1

	#Sin movimientos?
	if candidato > candidato_max:
		candidato, paso, historial_posiciones, tablero, aux = retroceder(paso, historial_posiciones, tablero, aux)

	solucion_encontrada, solucion = fin(salida, tablero)

	if solucion_encontrada == True:

		if solucion == True:
			solucion = False
			solucion_encontrada = False
			if modo_busqueda == "primer":
				print("La solucion si existe")
				#Muestra el tablero final
				guardar("solucion.txt","\n".join([str(k) for k in tablero]))
				print(f"\n".join([str([str(i) for i in tablero][x]) + str([str(e) for e in aux][x]) for x in range(m)])) # Muestra el tablero y el tablero auxiliar
				break
			elif modo_busqueda == "todas":
				lista_soluciones.append(copy.deepcopy(tablero)) #Independiza las 2 variables, sin eso no funciona
				candidato, paso, historial_posiciones, tablero, aux = retroceder(paso, historial_posiciones, tablero, aux)
				#guardar(str("\n".join([str(i) for i in tablero]))+"\n\n")
			elif modo_busqueda == "mejor":
				if paso < mejor_tiempo:
					mejor_tiempo = paso
					mejor_tablero = copy.deepcopy(tablero) #Independiza las 2 variables, sin eso no funciona
		elif solucion == False:
			if modo_busqueda == "primer":
				print("No existe solucion")
				break
			elif modo_busqueda == "todas":
				if len(lista_soluciones) > 0:
					print("Se han encontrado", str(len(lista_soluciones)), "soluciones")
					guardar("solucion.txt" ,str("\n\n".join([str(i) for i in ["\n".join([str(k) for k in j]) for j in lista_soluciones]])))
					#Insertar sistema de guardado, usa lista_soluciones donde estan guardadas todas las soluciones encontradas
				else:
					print("No se ha encontrado ninguna solucion")
			elif modo_busqueda == "mejor":
				if len(mejor_tablero) > 0:
					print(mejor_tiempo)
					print(f"\n".join([str(i) for i in mejor_tablero])) # Muestra el tablero y el tablero auxiliar
					guardar("mejor_solucion.dat","\n".join([str(k) for k in mejor_tablero]))
				else:
					print("No se ha encontrado ninguna solucion")
			break
