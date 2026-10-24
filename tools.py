#Aqui permanecen funciones que pueden ser reutilizadas

#Comprobar si posicion esta dentro de tablero MxN
def dentro_tablero(pos:tuple,m:int,n:int):
	fila, columna = pos
	if not 0 <= fila < m:
		return False
	if not 0 <= columna < n:
		return False
	return True

#Crea una matriz nula de MxN
def matriz_nula(m:int,n:int):
	matriz = []
	for fila in range(m):
		aux = []
		for columna in range(n):
			aux.append(0)
		matriz.append(aux)
	return matriz

#mostrar tablero
def mostrar_tablero(tablero:list):
	for i in tablero:
		print(i)

def preguntar_numero(text:str):
	while True:
		respuesta = input(text)
		if respuesta.isnumeric():
			numero = int(respuesta)
			return numero
		else:
			print("Por favor ingrese un numero")

def preguntar_opciones(opciones:list):
	for n in range(1,len(opciones)+1):
		print(f"{n}.{opciones[n-1]}")
	while True:
		respuesta = preguntar_numero(f"1-{len(opciones)+1}> ")
		if respuesta in range(1,len(opciones)+1):
			return respuesta
		else:
			print("Opcion fuera de rango")

import time
def tomar_frecuencia(ref:float,conteo:int):
	conteo += 1
	if (time.time()-ref) >=1:
		ref = time.time()
		print(conteo)
		conteo = 0
	return conteo, ref


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

def escribir_ssi_nuevo(file_name, soluciones)
	referencia = leer(file_name).split("N")
	n_registradas = []
	for i in referencia:
		i = i.split("\n")[0]
		i = i.strip("=")
		if i.isnumeric():
			n_registradas.append(int(i))

	if not n in n_registradas: #solucion no anotada
		with open(f"{file_name}.txt","a") as file:
			file.write("\n")
			file.write("N="+str(n))
			file.write("\n")
			for fila in soluciones[0]:
				file.write(str(fila).strip("[]"))
				file.write("\n")




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
