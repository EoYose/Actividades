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
if __name__ == "__main__":
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
