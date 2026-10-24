import random

##############################
#Herramientas basicas
##############################

#Arreglo aleatorio--------------------------------
if True:
	def crear_arreglo_aleatorio_iterativo(n):
		dominio = [i for i in range(n+1)]
		arreglo = []
		for i in range(n):
			arreglo.append(dominio.pop(random.randint(1,len(dominio)-1)))

	def crear_arreglo_aleatorio_recursivo(n,arreglo,dominio):
		#dominio = [i for i in range(n+1)]
		#arreglo = []
		if len(arreglo) < n:
		#for i in range(n):
			arreglo.append(dominio.pop(random.randint(1,len(dominio)-1)))
			arreglo = crear_arreglo_aleatorio_recursivo(n,arreglo, dominio)
		return arreglo

	def principal_crear_arreglo_aleatorio_recursivo(n):
		return crear_arreglo_aleatorio_recursivo(n,[],[i for i in range(n+1)])
#Imprimir--------------------------------
if True:
	def imprimir_iterativo(texto):
		n = len(texto)
		for i in range(n):
			print(texto[i])

	def principal_imprimir_recursivo(texto):
		imprimir_recursivo(texto,0)

	def imprimir_recursivo(texto="",i=0):
		n = len(texto)
		if i < n:
			print(texto[i])
			imprimir_recursivo(texto,i+1)
#sumar--------------------------------
if True:
	def sumar_iterativo(arreglo):
		n = len(arreglo)
		suma = 0
		for i in range(0,n):
			suma += arreglo[i]
		return suma

	def principal_sumar_recursivo(arreglo):
		return sumar_recursivo(arreglo,0)

	def sumar_recursivo(arreglo,suma):
		n = len(arreglo)
		if len(arreglo) > 0:
			suma += arreglo.pop(0)
			suma = sumar_recursivo(arreglo, suma)
		return suma
#determinar par--------------------------------
if True:
	def determinar_par(n):
		return n%2==0

	def determinar_par_iterativo(n):
		while n > 1:
			n -= 2
		return n == 0

	def determinar_par_recursivo(n):
		if n > 1:
			n -= 2
			n = determinar_par_recursivo(n)
		else:
			n = n == 0
		return n
#contar y sumar pares--------------------------------
if True:
	def contar_y_sumar_pares_iterativo(arreglo):
		conteo = 0
		suma = 0
		for i in arreglo:
			if determinar_par_iterativo(i):
				conteo+=1
				suma+=i
		return conteo, suma

	def principal_contar_y_sumar_pares_recursivo(arreglo):
		return contar_y_sumar_pares_recursivo(arreglo,0,0)

	def contar_y_sumar_pares_recursivo(arreglo, conteo, suma):
		if len(arreglo)>0: #verifica que todavia quede por revisar
			n = arreglo.pop(0) # elimina el elemento
			if determinar_par_recursivo(n):
				conteo+=1
				suma+=n
			#envia el arreglo reducido
			conteo, suma = contar_y_sumar_pares_recursivo(arreglo, conteo, suma)
		return conteo, suma #cuando se resolvio la ultima recursion
#contar y sumar impares--------------------------------
if True:
	def contar_y_sumar_impares_iterativo(arreglo):
		conteo = 0
		suma = 0
		for i in arreglo:
			if not determinar_par_iterativo(i):
				conteo+=1
				suma+=i
		return conteo, suma

	def principal_contar_y_sumar_impares_recursivo(arreglo):
		return contar_y_sumar_impares_recursivo(arreglo,0,0)

	def contar_y_sumar_impares_recursivo(arreglo, conteo, suma):
		if len(arreglo)>0: #verifica que todavia quede por revisar
			n = arreglo.pop(0) # elimina el elemento
			if not determinar_par_recursivo(n):
				conteo+=1
				suma+=n
			#envia el arreglo reducido
			conteo, suma = contar_y_sumar_impares_recursivo(arreglo, conteo, suma)
		return conteo, suma #cuando se resolvio la ultima recursion


######################################
#ORDENAR ARREGLO
######################################

#-------------------------------------
#SELECCION
if True:
	def ordenar_iterativo_seleccion(arreglo):
		n = len(arreglo)
		for i in range(0,n):
			for j in range(0,n):
				if arreglo[i] < arreglo[j]:
					arreglo[i],arreglo[j]=arreglo[j],arreglo[i]
		return arreglo

	def principal_ordenar_recursivo_seleccion(arreglo):
		return ordenar_recursivo_seleccion(arreglo,0,0)

	def ordenar_recursivo_seleccion(arreglo,i,j):
		n = len(arreglo)
		if i<n:
			if j<n:
				if arreglo[i] > arreglo[j]:
					arreglo[i],arreglo[j]=arreglo[j],arreglo[i]
				arreglo = ordenar_recursivo_seleccion(arreglo,i,j+1)
			else:
				arreglo = ordenar_recursivo_seleccion(arreglo,i+1,i+2)
		return arreglo

#-------------------------------------
#INSERCION 
if True:
	def ordenar_iterativo_insercion(arreglo):
		n = len(arreglo)
		for i in range(n):
			clave = arreglo[i]
			j = i -1
			#Desplaza los elementos mayores que la clave hacia la derecha
			while j >= 0 and clave < arreglo[j]:
				arreglo[j+1] = arreglo[j]
				j-=1
			#Inserta la clave en el hueco correspondiente
			arreglo[j+1] = clave
		return arreglo

	def principal_ordenar_recusivo_insercion(arreglo):
		return ordenar_recusivo_insercion(arreglo,1,0,arreglo[1])
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Red flag
#IndexError 
	def ordenar_recusivo_insercion(arreglo=[],i=1,j=0,clave=None):
		n = len(arreglo)
		if 0 < i < n:
			if j >= 0 and clave < arreglo[j]:
				arreglo[j+1] = arreglo[j]
				arreglo = ordenar_recusivo_insercion(arreglo, i,j-1,clave)
			else:
				arreglo[j+1] = clave
				arreglo = ordenar_recusivo_insercion(arreglo, i+1,i,arreglo[i+1])
		return arreglo

#-------------------------------------
#BURBUJA
if True:
	def ordenar_iterativo_burbuja(arreglo):
		n = len(arreglo)
		#realiza varias pasadas
		for i in range(n):
			for j in range(n-1):
				#Compara el proximo y lo ordena
				if arreglo[j] > arreglo[j+1]:
					arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
		return arreglo

	def principal_ordenar_recursivo_burbuja(arreglo):
		return ordenar_recursivo_burbuja(arreglo,0,0)

	def ordenar_recursivo_burbuja(arreglo, i=0, j=0):
	    n = len(arreglo)

	    if n < 2 or i >= n - 1:
	        return arreglo

	    if j < n - 1:
	        if arreglo[j] > arreglo[j + 1]:
	            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

	        return ordenar_recursivo_burbuja(arreglo, i, j + 1)

	    return ordenar_recursivo_burbuja(arreglo, i + 1, 0)

#-------------------------------------
#SHELLSORT
if True:
	def shell_sort_iterativo(lista):
		n = len(lista)
		salto = n // 2
		while salto > 0:
			i = salto
			while i <n:
				temp = lista[i]
				j=i
				while j >= salto and lista[j - salto]> temp:
					lista[j] = lista[j-salto]
					j -= salto
				lista[j] = temp
				i+=1
			salto //= 2
		return lista

	def principal_shell_sort_recursivo(lista):
		salto = len(lista)//2
		return shell_sort_recursivo(lista,salto)

	def shell_sort_recursivo(lista, salto):
		def aux2(lista, salto, j, temp):
			if j >= salto and lista[j - salto]> temp:
				lista[j] = lista[j-salto]
				j -= salto #modificacion
				lista = aux2(lista,salto,j,temp)
			else:
				lista[j] = temp
			return lista
		def aux(lista,salto,i):
			if i < n:
				temp = lista[i] #constante dependiente
				j=i #variable dependiente
				lista = aux2(lista,salto,j,temp)
				lista = aux(lista,salto,i+1)
			return lista
			
		n = len(lista) #constante
		if not salto > 0:
			return lista
		i = salto #variable dependiente
		if i <n:
			lista = aux(lista,salto,i)
		lista = shell_sort_recursivo(lista, salto//2)
		return lista

#-------------------------------------
#QUICKSORT

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Red flag
#Entrada: [6, 5, 8, 0, 10, 2, 9, 3, 1, 4]
#Salida: [1, 0, 2, 3, 4, 6, 9, 8, 10, 5]
def quick_sort_recursivo(lista):
	def aux(lista,i,j):
		n = len(lista)
		piv = lista[n-1]
		if i < n-1:
			i +=1
			if lista[i] <= piv:
				j+=1
				if i > j:
					lista[i], lista[j] = lista[j], lista[i]
			lista, j = aux(lista,i,j)
		return lista, j
	i=0
	j=-1
	n = len(lista)
	if n == 1:
		return lista

	lista, j = aux(lista,i,j)

	a,b = lista[0:j],lista[j+1:n]
	if len(a) >= 1:
		av = quick_sort_recursivo(a)
		lista[0:j] = av
	if len(b) >= 1:
		bv = quick_sort_recursivo(b)
		lista[j+1:n] = bv

	return lista


#################################
#CONTROL DE ENTRADAS DEL USUARIO
#################################
def preguntar_numero(text:str):
	while True:
		respuesta = input(text)
		if respuesta.isnumeric():
			numero = int(respuesta)
			return numero
		else:
			print("Por favor ingrese un numero")

def preguntar_opciones(opciones:list):
	for n in range(1,len(opciones)+1):
		print(f"{n}.{opciones[n-1]}")
	while True:
		respuesta = preguntar_numero(f"1-{len(opciones)}> ")
		if respuesta in range(1,len(opciones)+1):
			return respuesta
		else:
			print("Opcion fuera de rango")


if __name__ == "__main__":
	iterativo = [crear_arreglo_aleatorio_iterativo, 
	imprimir_iterativo, 
	sumar_iterativo, 
	determinar_par_iterativo, 
	contar_y_sumar_impares_iterativo,
	contar_y_sumar_impares_iterativo,
	ordenar_iterativo_seleccion,
	ordenar_iterativo_insercion,
	ordenar_iterativo_burbuja,
	shell_sort_iterativo]
	
	recursivo = [principal_crear_arreglo_aleatorio_recursivo,
	principal_imprimir_recursivo,
	principal_sumar_recursivo,
	determinar_par_recursivo,
	principal_contar_y_sumar_pares_recursivo,
	principal_contar_y_sumar_impares_recursivo,
	principal_ordenar_recursivo_seleccion,
	principal_ordenar_recusivo_insercion,
	principal_ordenar_recursivo_burbuja,
	principal_shell_sort_recursivo,
	quick_sort_recursivo
	]
	iterativo_ordenar = iterativo[6:9+1]
	recursivo_ordenar = recursivo[6:10+1]

	respuesta = preguntar_opciones(["Iterativo", "Recursivo"])
	def corregir(text, eliminar):
		for i in eliminar:
			text = text.replace(i, "")
		return text.replace("_"," ")	
	
	arreglo = principal_crear_arreglo_aleatorio_recursivo(preguntar_numero("Tamaño del arreglo: "))
	print("Arreglo creado:", arreglo)
	match respuesta:
		case 1:
			respuesta = preguntar_opciones([corregir(i.__name__,["iterativo"]) for i in iterativo_ordenar])
			print(iterativo_ordenar[respuesta-1](arreglo))
		case 2:
			respuesta = preguntar_opciones([corregir(i.__name__,["principal","recursivo"]) for i in recursivo_ordenar])
			print(recursivo_ordenar[respuesta-1](arreglo))


	exit()
	arreglo_original = [8,3,4,2,7,1,5]
	print("Antes")
	imprimir_recursivo(arreglo_original, 0)
	#nuevo_arreglo = ordenar_recursivo_burbuja(arreglo_original,0)
	nuevo_arreglo = ordenar_iterativo_insercion(arreglo_original)
	#nuevo_arreglo = ordenar_recusivo_insercion(arreglo_original,1,0,clave=arreglo_original[1])
	print("Despues")
	imprimir_recursivo(nuevo_arreglo, 0)

	input("Enter para salir..")