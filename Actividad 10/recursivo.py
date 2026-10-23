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
			arreglo.append(dominio.pop(random.randint(0,len(dominio)-1)))

	def crear_arreglo_aleatorio_recursivo(n,arreglo,dominio):
		#dominio = [i for i in range(n+1)]
		#arreglo = []
		if len(arreglo) < n:
		#for i in range(n):
			arreglo.append(dominio.pop(random.randint(0,len(dominio)-1)))
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

	def imprimir_recursivo(texto="",i=0):
		n = len(texto)
		if i < n:
			print(texto[i])
			imprimir(texto,i+1)
#sumar--------------------------------
if True:
	def sumar_iterativo(arreglo):
		n = len(arreglo)
		suma = 0
		for i in range(0,n):
			suma += arreglo[i]
		return suma

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

	def ordenar_recursivo_burbuja(arreglo, i=0, j=0):
	    n = len(arreglo)

	    if n < 2 or i >= n - 1:
	        return arreglo

	    if j < n - 1:
	        if arreglo[j] > arreglo[j + 1]:
	            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

	        return ordenar_recursivo_burbuja(arreglo, i, j + 1)

	    return ordenar_recursivo_burbuja(arreglo, i + 1, 0)

print(ordenar_recursivo_burbuja([6,2,3,1,5,4]))
exit()

#-------------------------------------
#SHELLSORT
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

print(principal_shell_sort_recursivo([5,2,1,4,3]))
exit()
#-------------------------------------
#QUICKSORT
 


if __name__ == "__main__":

	arreglo_original = [8,3,4,2,7,1,5]
	print("Antes")
	imprimir(arreglo_original, 0)
	#nuevo_arreglo = ordenar_recursivo_burbuja(arreglo_original,0)
	nuevo_arreglo = ordenar_iterativo_insercion(arreglo_original)
	#nuevo_arreglo = ordenar_recusivo_insercion(arreglo_original,1,0,clave=arreglo_original[1])
	print("Despues")
	imprimir(nuevo_arreglo, 0)

	input("Enter para salir..")