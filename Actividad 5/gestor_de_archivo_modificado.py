#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)
from pathlib import Path
ruta = Path(".")
def obtener_archivos():
	archivos = []
	for elemento in ruta.iterdir():
		if elemento.is_file():
			archivos.append(elemento.name)
	return archivos

def abrir(nombre,modo,contenido=None):
	with open(nombre,modo) as archivo:
		match modo:
			case "r":
				print("contenido del archivo")
				contenido = archivo.read()
				print(contenido)
				return contenido
			case "a":
				print("Ingrese contenido a anexar")
				contenido = input()
				archivo.write("\n"+contenido)
				print("<< Contenido anexado exitosamente")
			case "w":
				if contenido ==None:
					print("Ingrese contenido a escribir")
					contenido = input().split(";")
				archivo.write("\n".join(contenido))
				print("<< Contenido escrito exitosamente")

def eliminar(nombre):
	archivo = Path(nombre)
	archivo.unlink()
	print("<<Archivo Eliminado exitosamente")

def copiar(nombre, destino):
	destino = open(destino,"w+")
	origen = open(nombre, "r")
	destino.write(origen.read())
	destino.close()
	origen.close()
	print("<< Archivo copiado exitosamente")

def eliminar_registro(archivo, persona):
	lista_nueva = []
	with open(archivo,"r") as file:
		lista = file.read().split("\n")
		print("Registros")
		print(lista)
	for elemento in lista:
		if not elemento == persona:
			lista_nueva.append(elemento)
		else:
			print(persona, "eliminad@")
	with open(archivo,"w") as file:
		file.write("\n".join(lista_nueva))

	
def ordenar_ap(lista):
    lista2 = []

    for elemento in lista:
        lista2.append(elemento.strip().split())

    lista2.sort(key=lambda L: L[1])

    lista_ordenada = []

    for elemento in lista2:
        lista_ordenada.append(" ".join(elemento))

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
		print("6.eliminar_elemento")
		print("7.Ordenar")
		print("8.Salir (exit)")
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
			elif opcion == 6:
				print("Ingrese contenido del elemento a eliminar")
				busqueda = input(">")
				eliminar_registro(nombre,busqueda)
			#Ordenar
			elif opcion == 7:
				with open(nombre,"r") as archivo:
					lectura = archivo.readlines()
					print(lectura)
				lectura = ordenar_ap(lectura)
				print(lectura)
				abrir(nombre,"w",lectura)
				
			#salir del programa
			elif opcion == 8:
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
				contenido = input().split(";")
				archivo.write("\n".join(contenido))