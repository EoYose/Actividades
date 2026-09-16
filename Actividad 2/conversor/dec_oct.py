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
if __name__ == "__main__":
	while True:
		numero = input("Decimal: ")
		if numero.isnumeric():
			print("Octal: " + str(round(dec_to_oct(int(numero)))))
		else:
			print("Numero invalido")