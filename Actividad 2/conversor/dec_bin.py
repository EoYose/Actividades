#Conversion de decimal a binario mediante divisiones por 2
def decbin(dec):
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

def main():
	while True:
		numero = input("Ingrese numero: ").replace(" ", "")
		if numero.isnumeric():
			numero = int(numero)
			break
		else:
			print("Numero Invalido. Por favor no ingresar letras en el numero")
	binario = decbin(numero)
	print(f"Numero Decimal: {numero}\nNumero Binario: {''.join(binario)}\nCantidad de Bits: {len(binario)}") 

if __name__ == "__main__":
	print("Conversor de numero decimal a binario")
	while True:
		main()
		print("\n")