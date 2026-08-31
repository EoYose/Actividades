import random
def barcos_aleatorios(equipo):
	for i in ["portaaviones","destructor","fragata"]:
		for _ in range(3):
			while True:
				pos = (random.randint(1,10), random.randint(1,10))
				rotacion = random.choice(["arriba","abajo","izquierda","derecha"])
				largo = largo_tipo(i)
				if equipo.verificar_casillas(pos,largo, rotacion):
					if equipo.verificar_barcos(pos, largo, rotacion):
						equipo.añadir_barco(i, pos, rotacion)
						break
	return equipo
def desplazamiento(pos, largo, rotacion):
	fila, columna = pos
	match rotacion:
		case "arriba":
			fila -= largo
		case "abajo":
			fila += largo
		case "izquierda":
			columna -= largo
		case "derecha":
			columna += largo 
	return (fila, columna)
def largo_tipo(tipo):
	if tipo == "portaaviones":
		largo = 5
	elif tipo == "destructor":
		largo = 3
	elif tipo == "fragata":
		largo = 2
	else:
		largo = 1
	return largo
def preguntar_turno():
	print(f"Elija su turno \n1.Empiezas primero\n2.Empiezas segundo")
	while True:
		x = input(">>Turno: ")
		if x == "1" or x == "2":
			turno = int(x)-1
			break
		else:
			print("<<Entrada Invalida")
	return turno
def preguntar_barco():
	while True:
		barco = input(">>Barco: ")
		if barco.isnumeric():
			n = int(barco)
			barco = ""
			if n == 1:
				barco = "portaaviones"
				return barco, n	
			elif n == 2:
				barco = "destructor"
				return barco, n	
			elif n == 3:
				barco = "fragata"
				return barco, n	
			elif n == 4:
				return 4,4
			else:
				print("<<Entrada Invalida")
		else:
			print("<<Entrada Invalida")
def preguntar_fila_columna():
	pred = "<<Entrada no valida, por favor ingrese"
	print("Ingrese Fila")
	while True:
		fila = input(">>Fila: ")
		if not fila.isnumeric():
			print(pred, "un numero")
		else:
			fila = int(fila)
			if not fila in range(1,11):
				print(pred, "un numero del 1 al 10")
			else:
				break
	print("Ingrese Columna")
	while True:
		columna = input(">>Columna: ")
		if not columna.isnumeric():
			print(pred, "un numero")
		else:
			columna = int(columna)
			if not columna in range(1,11):
				print(pred, "un numero del 1 al 10")
			else:
				break
	return (fila,columna)
def preguntar_rotacion():
	print("Elija una rotacion.\n1.arriba\n2.abajo\n3.izquierda\n4.derecha")
	while True:
		rotacion = input(">>Rotacion: ")
		if rotacion.isnumeric():
			rotacion = int(rotacion)
			if 1 <= rotacion <= 4:
				rotacion = ["arriba", "abajo", "izquierda", "derecha"][rotacion-1]
				break
			else:
				print("<< Rotacion invalida") 
		else:
			if rotacion in ["arriba", "abajo", "izquierda", "derecha"]:
				break
			else:
				print("<< Rotacion Invalida.")
	return rotacion
def verificar_casilla(pos,tamaño_tabla):
	return 1 <= pos[0] <= tamaño_tabla[0] and 1 <= pos[1] <= tamaño_tabla[1]

class Barco:
	def __init__(self, tipo, pos, rotacion):
		self.pos = pos
		self.hundido = False
		self.tiros = 0
		self.rotacion = rotacion
		self.tipo = tipo
		self.largo = largo_tipo(tipo)
		self.area = []
		for i in range(0,self.largo):
			self.area.append(desplazamiento(self.pos,i,self.rotacion))

	def detectar_choque(self,pos):
		return pos in self.area
	def atacar(self,pos):
		if self.detectar_choque(pos):
			self.tiros += 1
			if self.tiros >= self.largo:
				self.hundido = True
				print("Se ha hundido un",self.tipo)
			return True
		return False
	def consultar_hundido(self):
		return self.hundido
class Equipo:
	def __init__(self):
		self.barcos = []
		self.tablero = []
	def inicializar_tablero(self,m,n):
		self.tablero = [["_"]*n for _ in range(m)]
	def mostrar_tablero(self,):

		print("  1|2|3|4|5|6|7|8|9|10")
		for n, i in enumerate(self.tablero):
			if n>8:
				print(str(n+1)+"|".join(i))
			else:
				print(str(n+1),"|".join(i))
	def visibilizar_barcos(self):
		for barco in self.barcos:
			for fila, columna in barco.area:
				if barco.tipo == "portaaviones":
					tipo = "P"
				elif barco.tipo == "destructor":
					tipo = "D"
				elif barco.tipo == "fragata":
					tipo = "F"
				self.tablero[fila-1][columna-1] = tipo
	def ocultar_barcos(self):
		for fila,i in enumerate(self.tablero):
			for columna,j in enumerate(i):
				if j in ["P","D","F"]:
					self.tablero[fila][columna] = "_"
	def añadir_barco(self, tipo, pos, rotacion):
		self.barcos.append(Barco(tipo,pos,rotacion))
	def ser_atacado(self, pos):
		for barco in self.barcos:
			if barco.atacar(pos):
				if barco.consultar_hundido():
					for fila, columna in barco.area:
						self.tablero[fila-1][columna-1] = "H"
				return barco
		return None
	def perder(self):
		a = 0
		for i in self.barcos:
			if i.hundido:
				a += 1
		if a >= len(self.barcos):
			return True
		return False
	def verificar_casillas(self,pos,largo,rotacion):
		tamaño_tabla = (10,10)
		return verificar_casilla(pos,tamaño_tabla) and verificar_casilla(desplazamiento(pos,largo-1,rotacion),tamaño_tabla)
	def verificar_barcos(self,pos,largo,rotacion):
		for i in range(0,largo):
			cf = desplazamiento(pos,i,rotacion)
			for j in self.barcos:
				if j.detectar_choque(cf):
					return False
		return True

mis_barcos = Equipo()
barcos_enemigos = Equipo()
mis_barcos.inicializar_tablero(10,10)
barcos_enemigos.inicializar_tablero(10,10)

turno = preguntar_turno()

#Elegir Barcos
aux = [3,3,3]
while any(aux):
	print(f"""Elija barco
Barcos disponibles:
1.Porta aviones (5 casillas) ({aux[0]} disponibles)
2.Destructor (3 casillas) ({aux[1]} disponibles)
3.Fragata (2 casillas) ({aux[2]} disponibles)
4.Aleatorio (inicio rapido)""")
	barco, barco_n = preguntar_barco()
	if barco == 4 and barco_n == 4:
		mis_barcos.barcos = []
		mis_barcos = barcos_aleatorios(mis_barcos)
		break
	if 0 == aux[barco_n-1]:
		print("<<Barco agotado")
		continue

	

	#Posicion barco
	print(f"Elija la posicion de su {barco}")
	fila, columna = preguntar_fila_columna()
	
	#Rotacion barco
	rotacion = preguntar_rotacion()

	#Verificacion de barco
	largo = largo_tipo(barco)
	if mis_barcos.verificar_casillas((fila,columna),largo,rotacion):
		if mis_barcos.verificar_barcos((fila,columna), largo, rotacion):
			mis_barcos.añadir_barco(barco, (fila,columna), rotacion)
			aux[barco_n-1] -= 1
			print("<<Barco colocado")
		else:
			print("<<Barco Superpuesto")
	else:
		print("<<Barco fuera de mapa")

#Crear barcos enemigos
barcos_enemigos = barcos_aleatorios(barcos_enemigos)

mis_barcos.visibilizar_barcos()
barcos_enemigos.mostrar_tablero()
ver_barcos_enemigos = False
if ver_barcos_enemigos:
	barcos_enemigos.visibilizar_barcos()

#Inicia el juego
while True:
	if turno == 0:
		print("es tu turno")
		print(f"Elija la posicion de su ataque")
		while True:
			fila,columna = preguntar_fila_columna()
			if verificar_casilla((fila,columna),(10,10)):
				break
			else:
				print("<<Casillas fuera del tablero")
		#Verificar casilla ya atacada
		if not barcos_enemigos.tablero[fila-1][columna-1] in "XOH":
			#atacar
			barco = barcos_enemigos.ser_atacado((fila,columna))
			if barco:
				if not barco.consultar_hundido():
					print("Le has dado a un barco")
					barcos_enemigos.tablero[fila-1][columna-1] = "X"
				turno = (turno+1)%2
			else:
				barcos_enemigos.tablero[fila-1][columna-1] = "O"
				print("No le has dado a nada")
		else:
			print("<<Casilla ya atacada, has perdido el turno")
		print("-----Tablero Enemigo-----")
		barcos_enemigos.mostrar_tablero()
	else:
		#Maquina ataca
		print("Es turno de la maquina")
		while True:
			#Patron de ataque aleatorio
			fila, columna = (random.randint(1,10), random.randint(1,10))
			if not mis_barcos.tablero[fila-1][columna-1] in "XOH":
				#atacar
				barcos = mis_barcos.ser_atacado((fila,columna))
				if barcos:
					if not barcos.consultar_hundido():
						print("La maquina acerto su ataque")
						mis_barcos.tablero[fila-1][columna-1] = "X"
					turno = (turno+1)%2
				else:
					mis_barcos.tablero[fila-1][columna-1] = "O"
					print("La maquina fallo su ataque")
				print("-----Tablero Jugador-----")
				mis_barcos.mostrar_tablero()
				break

	if mis_barcos.perder():
		print("Perdiste")
		break
	elif barcos_enemigos.perder():
		print("Ganaste")
		break

	turno = (turno+1)%2
input()