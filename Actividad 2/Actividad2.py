#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)

#Conversion de decimal a octal mediante divisiones por 8
def dec_oct(decimal):
	octal = 0
	base = 1
	while not decimal < 8:
		digito = decimal%8
		decimal -=digito
		octal += digito*base
		decimal /=8
		base*=10
	octal+=decimal*base
	return round(octal)
def main_dec_oct():
	while True:
		octal = input("Octal: ")
		if octal.isnumeric():
			if check_octal(octal):
				print("decimal: " + str(oct_dec(int(octal))))
			else:
				print("Numero octal fuera de rango")
		else:
			print("Numero invalido")

#Conversion de decimal a hexadecimal mediante divisiones por 16
def dec_hex(decimal):
	hexadecimal = ""
	hex_list = "0123456789ABCDEF"
	while not decimal < 16:
		digito = decimal%16
		#Descuenta el sobrante al decimal
		decimal -=digito
		#anexa el digito al hexadecimal 
		hexadecimal = hexadecimal + hex_list[digito]
		decimal = decimal//16
	hexadecimal = hex_list[decimal] + hexadecimal
	return hexadecimal
def main_dec_hex():
	while True:
		numero = input("Decimal: ")
		if numero.isnumeric():
			print("Hexadecimal " + str(dec_hex(int(numero))))
		else:
			print("Numero invalido")

#Conversion de decimal a octal mediante divisiones por 8
def dec_oct(decimal):
	octal = 0
	base = 1
	while not decimal < 8:
		digito = decimal%8
		decimal -=digito
		octal += digito*base
		decimal /=8
		base*=10
	octal+=decimal*base
	return round(octal)
def main_dec_oct():
	while True:
		numero = input("Decimal: ")
		if numero.isnumeric():
			print("Octal: " + str(round(dec_to_oct(int(numero)))))
		else:
			print("Numero invalido")

#Conversion de octal a decimal mediante multiplicaciones por 8
def oct_dec(octal):
	octal = int(octal)
	decimal = 0
	base = 1
	while not octal<8:
		digito = octal%10
		octal -= digito
		decimal = decimal + digito*base
		octal = octal//10
		base = base*8
	decimal = decimal + octal*base
	return decimal
#Verifica si el numero entregado es un octal valido
def check_octal(octal):
	for digito in str(octal):
		digito = int(digito)
		if digito > 8:
			return False
	return True
def main_oct_dec():
	while True:
		octal = input("Octal: ")
		if octal.isnumeric():
			if check_octal(octal):
				print("decimal: " + str(oct_dec(int(octal))))
			else:
				print("Numero octal fuera de rango")
		else:
			print("Numero invalido")

#Conversion de hexadecimal a decimal mediante multiplicaciones por 16
def hex_dec(hexadecimal):
	hexadecimal = hexadecimal.replace(" ","")
	hexadecimal = hexadecimal.upper()
	hex_chars = "0123456789ABCDEF"
	decimal = 0
	base = 1
	# range(Inicio, Fin, Paso)
	# hara que se vea de derecha a izquierda
	# Inicia en la derecha, termina en la izquierda y pasa a la izquierda 
	for n in range(len(hexadecimal)-1,-1,-1):
		aux = hexadecimal[n]
		if aux in hex_chars:
			aux1 = hex_chars.index(str(aux.upper()))
			decimal += aux1*base
			base*=16
		else:
			return None
	return decimal
def main_hex_dec():
	while True:
		hexadecimal = str(input("hexadecimal: "))
		decimal = hex_dec(hexadecimal)
		if decimal:
			print("decimal: " + str(decimal))
		else:
			print("Hexadecimal invalido")

#Conversion de decimal a binario mediante divisiones por 2
def dec_bin(dec):
	binario = 0
	vueltas = 0
	digito = 0
	while not dec <=1:
		digito = dec%2
		if digito == 1:
			dec-=1
		binario += digito*10**vueltas
		dec = dec//2
		vueltas += 1
	binario += dec*10**vueltas
	return str(binario)
def main_dec_bin():
	print("Conversor de numero decimal a binario")
	while True:
		while True:
			numero = input("Ingrese numero: ").replace(" ", "")
			if numero.isnumeric():
				numero = int(numero)
				break
			else:
				print("Numero Invalido. Por favor no ingresar letras en el numero")
		binario = dec_bin(numero)
		print(f"Numero Decimal: {numero}\nNumero Binario: {''.join(binario)}\nCantidad de Bits: {len(binario)}") 
	print("\n")

#Conversion de binario a decimal mediante multiplicaciones por 2
def bin_dec(binario):
	binario=int(binario)
	decimal = 0
	base = 1
	while not binario==0:
		digito = binario%10
		if digito == 1:
			binario = binario - 1
		decimal = decimal + digito*base
		binario = binario//10
		base = base*2
	return decimal
#verifica si el numero entregado es un binario valido
def check_if_bin(binario):
	aux = str(binario)
	for i in range(2,10):
		aux = aux.replace(str(i),"!")
	return aux == str(binario)
def main_bin_dec():
	print("Ingrese numero binario para trasnformarlo a numero decimal")
	while True:
		binario = input("Binario: ")
		if binario.isnumeric():
			if check_if_bin(binario):
				binario = int(binario)
				decimal = bin_dec(binario)
				print(decimal)
			else:
				print("Numero ingresado no es binario")
		else:
			print("solo numeros, no letras")

def main_toque_fama():
	#Toque y fama
	#fama -> el numero coincide en posicion
	#toque -> el numero no coincide en la posicion

	#Inicializacion
	import random
	#Numero mas alto a adivinar contando desde el 0
	n = 10

	#Crea una lista con numeros del 0 al 9 (n-1)
	dominio = [str(i) for i in range(n)]

	size = 5
	real = []

	#Crea la lista de numeros a adivinar
	#Va añadiendo un numero del dominio a la lista real de forma aleatoria
	#Elimina el numero del dominio para evitar que se repita
	for i in range(size):
		real.append(dominio.pop(dominio.index(random.choice(dominio))))

	def contar_toques_y_famas(real, prediccion):
		n_toque = 0
		n_fama = 0
		aux = []
		for n in range(len(prediccion)):
			#Comprueba si la prediccion atino en numero y posicion
			if prediccion[n] == real[n]:
				n_fama += 1
			#Comprueba si el numero esta dentro del real
			if prediccion[n] in real and not prediccion[n] in aux:
				n_toque += 1
				aux.append(i)

		#arreglar desfase
		#El desfase ocurre porque tecnicamente si es fama tambien es toque
		#Pero en el juego es toque o es fama
		n_toque -= n_fama
		return n_toque, n_fama

	def leer_jugador():
		while True: #Leer jugador
			print("Ingrese 5 numeros sin repetirse separados por comas. ")
			print("Ejemplo: 1,2,3,4,5")
			txt = input(">>> ") #Ejemplo 1,2,3,4,5
			txt = txt.split(",")
			prediccion = []
			for i in txt:
				prediccion.append(i.strip(" "))
			if len(prediccion) != size:
				print("tamaño incorrecto")
			else:
				if all([i.isnumeric() for i in prediccion]):
					break
				else:
					print("No se aceptan letras")
		return prediccion

	#Inicializa las variables del juego
	intentos = 5
	n_fama = 0
	n_toque = 0

	#Empieza juego
	while True:
		prediccion = leer_jugador()
		#detectar toques y famas
		n_toque, n_fama = contar_toques_y_famas(real,prediccion)
		
		#descontar intentos
		intentos -= 1
		#mostrar informacion
		print("Numero de toques:", n_toque)
		print("Numero de famas:", n_fama)
		print("Intentos restanes:", intentos)
			
		#condicion de victoria
		if n_fama == size:
			print("Ganaste")
			break
		#condicion de perdicion
		if intentos == 0:
			print("Perdiste")
			print("El numero era: ",real)
			break


while True:
	print("-------------------------")
	print("1.Decimal a binario")
	print("2.Binario a decimal")
	print("3.Decimal a octal")
	print("4.Octal a decimal")
	print("5.Decimal a hexadecimal")
	print("6.Hexadecimal a decimal")
	print("7.Juego Toque y fama")
	print("8.Salir")
	print("Elija programa a ejecutar")
	entrada = input(">")
	if not entrada.isnumeric():
		print("debe ser un numero")
		continue
	entrada = int(entrada)
	try:
		match entrada:
			case 1:
				main_dec_bin()
			case 2:
				main_bin_dec()
			case 3:
				main_dec_oct()
			case 4:
				main_oct_dec()
			case 5:
				main_dec_hex()
			case 6:
				main_hex_dec()
			case 7:
				main_toque_fama()
			case 8:
				exit()
			case _:
				print("Opcion fuera de rango, elija una valida")
	except KeyboardInterrupt:
		#Captura la combinacion ctrl + c
		#Permite salir de un programa del menu
		#Solo funciona en consola de python, no en consola de editor
		print("\n###################")
		print("Programa cancelado")
		print("###################")