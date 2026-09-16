#Realiza el proceso especifico para obtener el digito verificador
def digito_verificador(rut):
	factor=2;suma=0;aux=rut
	while True:
		aux1=aux//10
		aux1=aux1*10
		digito=aux-aux1
		suma=suma+(digito*factor)
		factor=factor+1
		if factor >= 8: factor = 2
		aux=aux1//10
		if aux ==0: break
	resto=suma%11
	dv = 11-resto
	if dv == 10: 
		dv ="K"
	elif dv == 11: 
		dv=0
	return dv
def main():
	while True:
		#Valida el rut
		rut = input("rut: ").replace(".","").replace(",","")
		if rut != rut.replace("-",""):
			print("Por favor ingresar sin digito verificador")
		elif rut.isnumeric():
			if len(rut) in [7,8]:
				break
			else:
				print("Largo del rut invalido")
		else:
			print("Letras no admitidas")
	#Obtiene el digito verificador
	dv = str(digito_verificador(int(rut)))
	if len(rut) == 8:
		#Añade los puntos al rut como normalmente seria si tubiera 8 digitos xx.xxx.xxx
		rut = ".".join([rut[0:2],rut[2:5],rut[5:8]])
	elif len(rut) == 8:
		#Añade los puntos al rut como normalmente seria si tubiera 7 digitos x.xxx.xxx
		rut = ".".join([rut[0:1],rut[1:4],rut[4:7]])
	print(f"Digito Verificador: {dv}\nRut Completo: {rut}-{dv}")
if __name__ == "__main__":
	print("Ingrese su rut sin su digito verificador para obtenerlo")
	while True:
		main()