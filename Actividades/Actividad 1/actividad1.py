def dias_de_un_mes(dia,mes,año):
	#Obtiene cuantos dias hay en un mes
	if mes in [1,3,5,7,8,10,12]:
		n=31
	if mes in [4,6,9,11]:
		n=30
	if mes == 2:
		#condicion año bisiesto
		if (año%4) == 0  and not (año%100) == 0 or (año%400) == 0:
			n = 29
		else:
			n = 28
	#Comprueba que la fecha sea una valida
	if mes > 12 or mes < 1:
		return None
	if dia > n or dia < 1:
		return None
	else:
		return n
def dia_siguiente(diaxmes,dia,mes,año):
	#avanza al dia siguiente
	dia+=1
	#asegura que el dia siguiente este dentro del mes
	if dia > diaxmes:
		mes +=1
		dia = 1
	#asegura que el mes siguiente este dentro del año
	if mes > 12:
		año+=1
		mes=1
	return dia,mes,año
def main_diasiguiente():
	#Recepcion de informacion y control
	auxsalida = False
	while not auxsalida:
		auxsalida = True
		fecha = input("Fecha: ")
		fecha = fecha.split("/")
		for i in fecha:
			if not i.isnumeric():
				print("se requieren solo numeros")
				auxsalida = False
		fecha = [int(i) for i in fecha]
		diaxmes = dias_de_un_mes(*fecha)
		if not diaxmes:
			print("Dia/Mes/Año fuera del rango esperado")
			auxsalida = False
	fecha_siguiente = dia_siguiente(diaxmes,*fecha)
	dia,mes,año = fecha_siguiente
	print(f"Dia proximo: {dia}/{mes}/{año}")


#Realiza el proceso especifico para obtener el digito verificador
def digito_verificador(rut):
	factor=2;suma=0;aux=rut
	while True:
		aux1=aux//10
		aux1=aux1*10
		digito=aux-aux1
		suma=suma+(digito*factor)
		factor=factor+1
		if factor >= 8: factor = 2
		aux=aux1//10
		if aux ==0: break
	resto=suma%11
	dv = 11-resto
	if dv == 10: 
		dv ="K"
	elif dv == 11: 
		dv=0
	return dv
def main_digito_v():
	while True:
		#Valida el rut
		rut = input("rut: ").replace(".","").replace(",","")
		if rut != rut.replace("-",""):
			print("Por favor ingresar sin digito verificador")
		elif rut.isnumeric():
			if len(rut) in [7,8]:
				break
			else:
				print("Largo del rut invalido")
		else:
			print("Letras no admitidas")
	#Obtiene el digito verificador
	dv = str(digito_verificador(int(rut)))
	if len(rut) == 8:
		#Añade los puntos al rut como normalmente seria si tubiera 8 digitos xx.xxx.xxx
		rut = ".".join([rut[0:2],rut[2:5],rut[5:8]])
	elif len(rut) == 8:
		#Añade los puntos al rut como normalmente seria si tubiera 7 digitos x.xxx.xxx
		rut = ".".join([rut[0:1],rut[1:4],rut[4:7]])
	print(f"Digito Verificador: {dv}\nRut Completo: {rut}-{dv}")




#verifica que la jugada sea valida
def verificar_jugada_valida(tablero, posicion):
	letras = "ABCDEFGHI"
	if posicion.upper() in letras:
		numero_posicion = letras.index(posicion.upper())
		if not tablero[numero_posicion].upper() in "XO":
			return numero_posicion + 1
		else:
			print("Posicion ya ocupada")
			return False
	else:
		print("Posicion Invalida")
		return False
#inicializa el tablero
def iniciar_tablero():
	tablero = list("ABCDEFGHI")
	return tablero
#muestra el tablero
def mostrar_tablero(tablero):
	t = tablero
	print(f"""
{t[0]} | {t[1]} | {t[2]}
{t[3]} | {t[4]} | {t[5]}
{t[6]} | {t[7]} | {t[8]}
""")
#Pregunta al usuario que ficha quiere segun el turno con que quiera empezar
def elegir_ficha():
	print("""
Elija Ficha:
1. Para X (hara que empieces primero)
2. Para O (hara que empieces segundo)
""")
	while True:
		ficha = input("Ficha: ").upper()
		if ficha.isnumeric():
			if int(ficha) == 1:
				ficha = "X"
				return ficha
			elif int(ficha) == 2:
				ficha = "O"
				return ficha
			else:
				print("Numero no valido")
		else:
			if ficha in "XO" and len(ficha) == 1:
				return ficha
			else:
				print("Entrada no valida")
#hace jugar a la maquina (juega en la primera casilla disponible)
def maquina_juega(tablero, ficha):
	disponibles = []
	for numero, casilla in enumerate(tablero):
		if not casilla in "XO":
			tablero[numero] = ficha
			return tablero
#hace jugar al jugador
def jugador_juega(tablero, ficha):
	mostrar_tablero(tablero)
	print("Elija posicion")
	while True:
		posicion = input("Posicion: ")
		posicion_numero = verificar_jugada_valida(tablero, posicion)
		if bool(posicion_numero) == True:
			tablero[posicion_numero-1] = ficha
			return tablero
#detecta condiciones de victoria
def detectar_victoria(tablero):
	t = tablero
	if t[0] == t[1] == t[2]:
		return True
	elif t[3] == t[4] == t[5]:
		return True
	elif t[6] == t[7] == t[8]:
		return True
	elif t[0] == t[3] == t[6]:
		return True
	elif t[1] == t[4] == t[7]:
		return True
	elif t[2] == t[5] == t[8]:
		return True
	elif t[0] == t[4] == t[8]:
		return True
	elif t[2] == t[4] == t[6]:
		return True
	else:
		return False
#detecta condiciones de empate
def detectar_empate(tablero):
	t = tablero
	if t.count("X") + t.count("O") == len(t):
		return True
	else:
		return False
#permite salir y preconfigurar acciones antes de salir
def salir():
	print("desea salir?")
	x = input("s/n").lower()
	if x.replace("s","") != x:
		exit()
	main_gatoenraya()
def main_gatoenraya():
	#Inicializacion
	tablero = iniciar_tablero()
	ficha = "X"
	ficha_jugador = elegir_ficha()
	if ficha_jugador == "X":
		ficha_maquina = "O"
	else:
		ficha_maquina = "X"
	#Inicio del juego
	while True:
		if ficha == ficha_jugador:
			#juega el jugador
			tablero = jugador_juega(tablero, ficha_jugador)
		elif ficha == ficha_maquina:
			#juega la maquina
			tablero = maquina_juega(tablero, ficha_maquina)
		mostrar_tablero(tablero)
		if detectar_victoria(tablero):
			if ficha == ficha_jugador:
				print("Has ganado")
				salir()
			else:
				print("Has perdido")
				salir()
		elif detectar_empate(tablero):
			print("Han empatado")
			salir()
		else:
			#Cambio de turno
			if ficha == "X":
				ficha = "O"
			else:
				ficha = "X"


while True:
	print("Elija uno de los siguientes programas")
	print("1.Dia siguiente")
	print("2.Digito verificador")
	print("3.Gato en raya")
	entrada = input(">")
	if not entrada.isnumeric():
		print("La entrada debe ser un numero")
		continue
	entrada = int(entrada)
	if not entrada in [1,2,3]:
		print("Entrada fuera del rango")
	if entrada == 1:
		print("Ingrese fecha dia/mes/año")  
		main_diasiguiente()
	elif entrada == 2:
		print("Ingrese su rut sin su digito verificador para obtenerlo")
		main_digito_v()
	elif entrada == 3:
		main_gatoenraya()
