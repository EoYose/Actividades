from pathlib import Path
ruta = Path(".")
def obtener_archivos():
	archivos = []
	for elemento in ruta.iterdir():
		if elemento.is_file():
			archivos.append(elemento.name)
	return archivos

def abrir(nombre,modo):
	with open(nombre,modo):
		match modo:
			case "r":
				print("contenido del archivo")
				contenido = archivo.read()
				print(contenido)
			case "a":
				print("Ingrese contenido a anexar")
				contenido = input()
				archivo.write(contenido)
				print("<< Contenido anexado exitosamente")
			case "w":
				print("Ingrese contenido a escribir")
				contenido = input()
				archivo.write(contenido)
				print("<< Contenido escrito exitosamente")

def eliminar(nombre):
	archivo = Path(nombre)
	archivo.unlink()
	print("<<Archivo Eliminado exitosamente")

def copiar(nombre, destino)
	archivo = Path(nombre)
	archivo.copy(destino)
	print("<< Archivo copiado exitosamente")

def ordenar_lista_por_abcedario(lista):
	abcedario = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	lista_ordenada = []
	for letra in abcedario:
		for elemento in lista:
			if elemento.upper().startwith(letra):
				lista_ordenada.append(elemento)
	return lista_ordenada

while True:
	nombre = input("Nombre de archivo: ")
	
	if nombre == Path(__file__).name:
		print("NO PUEDES MODIFICAR EL ARCHIVO QUE ESTA SIENDO EJECUTADO")
		print("por favor intenta con otro archivo")
		continue

	if nombre in obtener_archivos():
		print("Que accion desea hacer?")
		print("1.Leer (read)")
		print("2.Anexar (append)")
		print("3.Escribir (write)")
		print("4.Eliminar (delete)")
		print("5.Copiar (copy)")
		print("6.Salir (exit)")
		opcion = input("1/2/3/4/5: ")
		if opcion.isnumeric():
			opcion = int(opcion)
			#acceder al archivo
			if opcion in [1,2,3]:
				abrir(nombre,"raw"[opcion-1])
			#eliminar archivo
			elif opcion == 4:
				eliminar(nombre)
			#copiar archivo
			elif opcion == 5:
				print("Ingrese nombre del archivo destino")
				destino = input(">>> ")
				copiar(nombre, destino)
			#salir del programa
			elif opcion == 6:
				exit()
			else:
				print("Entrada invalida")
				continue

	else:
		#El archivo no existe, preguntar si desea crearlo
		print("Archivo no existente, desea crearlo?")
		y = input("s/n: ").lower()
		if "s" in y:
			with open(nombre,"w+") as archivo:
				print("Ingrese contenido a escribir")
				contenido = input()
				archivo.write(contenido)