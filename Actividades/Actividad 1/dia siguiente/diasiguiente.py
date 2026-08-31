def dias_de_un_mes(dia,mes,año):
	#Obtiene cuantos dias hay en un mes
	if mes in [1,3,5,7,8,10,12]:
		n=31
	if mes in [4,6,9,11]:
		n=30
	if mes == 2:
		#condicion año bisiesto
		if (año%4) == 0  and not (año%100) == 0 or (año%400) == 0:
			n = 29
		else:
			n = 28
	#Comprueba que la fecha sea una valida
	if mes > 12 or mes < 1:
		return None
	if dia > n or dia < 1:
		return None
	else:
		return n
def dia_siguiente(diaxmes,dia,mes,año):
	#avanza al dia siguiente
	dia+=1
	#asegura que el dia siguiente este dentro del mes
	if dia > diaxmes:
		mes +=1
		dia = 1
	#asegura que el mes siguiente este dentro del año
	if mes > 12:
		año+=1
		mes=1
	return dia,mes,año
def main():
	#Recepcion de informacion y control
	auxsalida = False
	while not auxsalida:
		auxsalida = True
		fecha = input("Fecha: ")
		fecha = fecha.split("/")
		for i in fecha:
			if not i.isnumeric():
				print("se requieren solo numeros")
				auxsalida = False
		fecha = [int(i) for i in fecha]
		diaxmes = dias_de_un_mes(*fecha)
		if not diaxmes:
			print("Dia/Mes/Año fuera del rango esperado")
			auxsalida = False
	fecha_siguiente = dia_siguiente(diaxmes,*fecha)
	dia,mes,año = fecha_siguiente
	print(f"Dia proximo: {dia}/{mes}/{año}")
if __name__ == "__main__":
	print("Ingrese fecha dia/mes/año")
	while True:
		main()