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
if __name__ == "__main__":
	while True:
		octal = input("Octal: ")
		if octal.isnumeric():
			if check_octal(octal):
				print("decimal: " + str(oct_dec(int(octal))))
			else:
				print("Numero octal fuera de rango")
		else:
			print("Numero invalido")