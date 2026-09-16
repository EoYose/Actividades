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
	main()
def main():
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