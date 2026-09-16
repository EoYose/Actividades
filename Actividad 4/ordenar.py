#Eliminar un registro
fd = open("alumnos.dat", "r")
aux_fd = open("temporal1.tmp","w")
nombre1, app1, apm1 = obtener_nombres()
while not eof(fd):
	leer_registro(nombre,app,apm)
	if nombre != nombre1 and app != app1 and apm != apm1::
		aux_fd.write(nombre,app,apm)
fd.close()
aux_fd.close()
copiar_file(aux_fd,"alumnos.dat")
eliminar_file(aux_fd)

#ordenar registros del archivo de menor a mayor
fd = "alumnos.dat"
aux1 = "auxiliar.tmp"
while not eof(fd):
	leer_registro(nombre,app,apm)
	agregar_registro_aux(nombre,app,apm, aux1)
copiar_file(aux1, fd)
eliminar_file(aux1)

def agregar_registro_aux(nombre, app, apm, aux1):
	aux2 = "auxiliar.tmp"
	while not eof(aux1):
		leer_registro(nombre_aux, app_aux, apm_aux)
		cadena1 = original
		cadena2 = registro_del_auxiliar
		if cadena1 == cadena2:
			#cadena1 > cadena2
			escribir_en_auxiliar2(aux2,nombre_aux,app_aux,apm_aux)
		else:
			escribir_en_auxiliar2(aux2,nombre,app,apm)
			nombre = nombre_aux
			app = app_aux
			apm = apm_aux
	copiar_file(aux2, aux1)
	eliminar_file(aux2)
	
def escribir(direccion, *argumentos):
	with open(direccion, "w") as archivo:
		archivo.write(argumentos)

def eliminar_file(direccion):
	if os.path.exist(direccion):
		os.remove(direccion)
	else:
		print('no existe el archivo')

def copiar_file(original, destino):
	archivo_original = open(original,"r")
	archivo_destinatario = open(destino,"w+")
	contenido_original = archivo_original.read()
	archivo_destinatario.write(contenido_original)
	archivo_original.close()
	archivo_destinatario.close()
