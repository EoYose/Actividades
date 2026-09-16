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
if __name__ == "__main__":
	while True:
		numero = input("Decimal: ")
		if numero.isnumeric():
			print("Hexadecimal " + str(dec_hex(int(numero))))
		else:
			print("Numero invalido")