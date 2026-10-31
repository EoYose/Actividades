import random
import sys

# Aumentar el límite a 3000 (o el número que necesites)
sys.setrecursionlimit(3000)


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
		if len(arreglo) < n:
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

	def principal_ordenar_recursivo_insercion(arreglo):
		return ordenar_recursivo_insercion(arreglo,1,0,arreglo[1])

	def ordenar_recursivo_insercion(arreglo=[],i=1,j=0,clave=None):
		n = len(arreglo)
		if 0 < i < n-1:
			if j >= 0 and clave < arreglo[j]:
				arreglo[j+1] = arreglo[j]
				arreglo = ordenar_recursivo_insercion(arreglo, i,j-1,clave)
			else:
				arreglo[j+1] = clave
				arreglo = ordenar_recursivo_insercion(arreglo, i+1,i,arreglo[i+1])
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
	i=-1 ; j=-1 #Indice basado en cero
	n = len(lista)
	if n <= 1:
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
#Busqueda Binaria
#################################
def principal_BBinario_recursiva(datos,valor):
	return BBinario_recursiva(datos,0,len(datos)-1,valor)

def BBinario_recursiva(datos,inicio,final,valor):
	if inicio < final:
		mitad = (inicio + final)//2
		if datos[mitad] == valor:
			return mitad
		else:
			if datos[mitad] > valor:
				final -= 1
			else:
				inicio += 1
			return BBinario_recursiva(datos,inicio,final,valor)
	return False


#################################
# Torres de Hanoi
#################################
#-------------Torres---------------
#o: origen #d: destino #a: auxiliar
#Representacion de las torres con arreglos:
#[5,4,3,2,1]
#suelo -> cima

if True:
	def hanoi_iterativo(n):
		total_moves = 2 ** n - 1
		# Índices: origen = 0, aux = 1, destino = 2
		rods = [list(range(n, 0, -1)), [], []]
		names = ['A', 'B', 'C']

		for move in range(1, total_moves + 1):
		    if move % 3 == 1:
		        a, b = 0, 1
		    elif move % 3 == 2:
		        a, b = 0, 2
		    else:
		        a, b = 1, 2

		    # Determinar el origen y el destino
		    if rods[a] and (not rods[b] or rods[a][-1] < rods[b][-1]):
		        from_rod, to_rod = a, b
		    else:
		        from_rod, to_rod = b, a

		    disk = rods[from_rod].pop()
		    rods[to_rod].append(disk)

		    print(
		        f"mover disco {disk} desde "
		        f"{names[from_rod]} hasta {names[to_rod]}"
		    )
		if len(rods[1]) > 0:
			rods[2] = rods[1]
			rods[1] = []
		return rods

	def principal_hanoi_recursivo(n):
		# Índices: origen = 0, aux = 1, destino = 2
		rods = [list(range(n, 0, -1)), [], []]
		ordenado = hanoi_recursivo(rods=rods,move = 1,total_moves = 2 ** n - 1)
		if len(ordenado[1]) > 0:
			ordenado[2] = ordenado[1]
			ordenado[1] = []
		return ordenado
	def hanoi_recursivo(rods,move,total_moves):
		names = ['A', 'B', 'C']
		if move < total_moves + 1:
		    if move % 3 == 1:
		        a, b = 0, 1
		    elif move % 3 == 2:
		        a, b = 0, 2
		    else:
		        a, b = 1, 2

		    # Determinar el origen y el destino
		    if rods[a] and (not rods[b] or rods[a][-1] < rods[b][-1]):
		        from_rod, to_rod = a, b
		    else:
		        from_rod, to_rod = b, a

		    disk = rods[from_rod].pop()
		    rods[to_rod].append(disk)

		    print(f"Mover disco {disk} desde ",f"{names[from_rod]} hasta {names[to_rod]}")

		    move += 1
		    rods = hanoi_recursivo(rods, move,total_moves)
		return rods

#################################
#SUBIENDO ESCALERAS
#################################

def escaleras_recursivo(n):
	if n <= 0:
		print("No hay peldaños por subir")
		return []
	if n == 1:
		return [[1]]
	if n == 2:
		return [[1,1],[2]]
	else:
		lista = [[1 for _ in range(n)]]
		for j in escaleras_recursivo(n-1):
			lista.append([1]+j)
		for j in escaleras_recursivo(n-2):
			lista.append([2]+j)
		if n%2 == 0:
			lista.append([2 for _ in range(n//2)])
	return lista

def limpiar_lista(lista, lista_limpia):
	if 0 < len(lista):
		elemento = lista.pop(0)
		if elemento not in lista_limpia:
			lista_limpia.append(elemento)
		lista_limpia = limpiar_lista(lista,lista_limpia)
	return lista_limpia

def principal_escaleras(n):
	return limpiar_lista(escaleras_recursivo(n),[])

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
	def corregir(text, eliminar):
		for i in eliminar:
			text = text.replace(i, "")
		return text.replace("_"," ")

	def comparar_funciones(funciones, arreglo):
		print(f"Arreglo original: {arreglo}")
		arreglo.sort()
		print(f"Arreglo ordenado: {arreglo}")
		for func in funciones:
			resultado = func(arreglo)
			print(f"funcion {func.__name__} {["no funciona", "funciona"][int(resultado == arreglo)]}")
			if resultado != arreglo:
				print(resultado)

	def verificar(arreglo, retorno):
		arreglo.sort()
		print(retorno)
		print(f"La solucion es {["incorrecta","correcta"][int(arreglo==retorno)]}")

	#iterativo = [crear_arreglo_aleatorio_iterativo, imprimir_iterativo, sumar_iterativo, determinar_par_iterativo, contar_y_sumar_impares_iterativo,contar_y_sumar_impares_iterativo,ordenar_iterativo_seleccion,ordenar_iterativo_insercion,ordenar_iterativo_burbuja,shell_sort_iterativo]
	#recursivo = [principal_crear_arreglo_aleatorio_recursivo,principal_imprimir_recursivo,principal_sumar_recursivo,determinar_par_recursivo,principal_contar_y_sumar_pares_recursivo,principal_contar_y_sumar_impares_recursivo,principal_ordenar_recursivo_seleccion,principal_ordenar_recursivo_insercion,principal_ordenar_recursivo_burbuja,principal_shell_sort_recursivo,quick_sort_recursivo]
	
	iterativo_ordenar = [ordenar_iterativo_seleccion, ordenar_iterativo_insercion, ordenar_iterativo_burbuja, shell_sort_iterativo]
	recursivo_ordenar = [principal_ordenar_recursivo_seleccion, principal_ordenar_recursivo_insercion, principal_ordenar_recursivo_burbuja, principal_shell_sort_recursivo, quick_sort_recursivo]
	

	respuesta = preguntar_opciones(["Ordenar",#1
	"Crear arreglo aleatorio",#2
	"Imprimir",#3
	"sumar",#4
	"determinar par",#5
	"sumar y contar pares",#6
	"sumar y contar impares",#7
	"busqueda Binaria",#8
	"Torres de hanoi",#9
 	"subir escaleras"#10
 	])
	if respuesta in [1,2,4,6,7]:
		arreglo = principal_crear_arreglo_aleatorio_recursivo(preguntar_numero("Tamaño del arreglo: "))
		print("Arreglo creado:", arreglo)
	
	match respuesta:
		case 1: #Ordenar Arreglo
			respuesta = preguntar_opciones(["Iterativo", "Recursivo"])
			match respuesta:
				case 1:
					respuesta = preguntar_opciones([corregir(i.__name__,["iterativo"]) for i in iterativo_ordenar]+["todas"])
					if respuesta > len(iterativo_ordenar):
						comparar_funciones(iterativo_ordenar,arreglo)
					else:
						retorno = iterativo_ordenar[respuesta-1](arreglo)
						verificar(arreglo,retorno)
				case 2:
					respuesta = preguntar_opciones([corregir(i.__name__,["principal","recursivo"]) for i in recursivo_ordenar]+["todas"])
					if respuesta > len(recursivo_ordenar):
						comparar_funciones(recursivo_ordenar,arreglo)
					else:
						retorno = recursivo_ordenar[respuesta-1](arreglo)
						verificar(arreglo,retorno)
		case 2:
			pass
		case 3:
			texto = input("Ingrese texto a imprimir: ")
			print("-"*5)
			principal_imprimir_recursivo(texto)
		case 4:
			print(f"suma: {principal_sumar_recursivo(arreglo)}")
		case 5:
			n = preguntar_numero("Numero: ")
			print(f"El numero {n} {["no",""][int(determinar_par_recursivo(n))]} es par")
		case 6:
			conteo, suma = principal_contar_y_sumar_pares_recursivo(arreglo)
			print(f"En el arreglo hay {conteo} numeros pares")
			print(f"y suman {suma}")
		case 7:
			conteo, suma = principal_contar_y_sumar_impares_recursivo(arreglo)
			print(f"En el arreglo hay {conteo} numeros impares")
			print(f"y suman {suma}")
		case 8:
			tamaño = preguntar_numero("Tamaño del arreglo: ")
			arreglo = crear_arreglo_aleatorio_recursivo(tamaño, [], [i//2 for i in range(1,tamaño+2)])
			print("Arreglo creado:", arreglo)
			arreglo_ordenado = quick_sort_recursivo(arreglo)
			print("Arreglo ordenado:", arreglo_ordenado)
			n = preguntar_numero("Buscar el numero")
			indice = principal_BBinario_recursiva(arreglo_ordenado,n)
			if indice == False:
				print("El numero no ha sido encontrado")
			else:
				print(f"El numero ha sido encontrado en el indice {indice}")
		case 9:
			resuelto = principal_hanoi_recursivo(preguntar_numero("Numero de aros de la torre de hanoi: "))
			print("Torre ordenada")
			print(resuelto)
		case 10:
			n = preguntar_numero("Cuantos peldaños tiene su escalera??? : ")
			print("Se puede subir la escalera subiendo 1 o 2 peldaños a la vez.")
			print("-"*20)
			formas = principal_escaleras(n)
			print(f"Se puede subir la escalera de {len(formas)} formas distintas")
			print("Desea ver las formas de subir la escalera?")
			if preguntar_opciones(["si","no"]) == 1:
				print("Formas", formas)

	input("Enter para salir..")