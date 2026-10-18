#Aqui permanecen funciones que pueden ser reutilizadas

#Comprobar si posicion esta dentro de tablero MxN
def dentro_tablero(pos,m,n):
	fila, columna = pos
	if not 0 <= fila < m:
		return False
	if not 0 <= columna < n:
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

#Ejemplo
if __name__ == "__main__":
	tablero = []
	m,n = -1,-1
	while True:
		print()
		print("#"*20)
		respuesta = preguntar_opciones(["crear tablero", "mostrar tablero", "consultar dentro tablero", "salir"])
		match respuesta:
			case 1:
				m, n = preguntar_numero("filas: "), preguntar_numero("columnas: ")
				tablero = matriz_nula(m,n)
			case 2:
				mostrar_tablero(tablero)
			case 3:
				pos = (preguntar_numero("X: "), preguntar_numero("Y: "))
				if m == -1 or n == -1:
					print("tablero no creado")
				else:
					print(f"{pos} {["no","si"][int(dentro_tablero(pos,m,n))]} esta dentro del tablero")
			case 4:
				break
