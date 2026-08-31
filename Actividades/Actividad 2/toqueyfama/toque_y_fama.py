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
