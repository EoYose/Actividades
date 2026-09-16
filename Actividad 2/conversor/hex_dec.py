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
if __name__ == "__main__":
	while True:
		hexadecimal = str(input("hexadecimal: "))
		decimal = hex_dec(hexadecimal)
		if decimal:
			print("decimal: " + str(decimal))
		else:
			print("Hexadecimal invalido")