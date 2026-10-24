El shell sort es una forma de ordenamiento que mejora el ordenamiento por insercion al ordenar elementos separados por cierta distancia (salto) y reducirla progresivamente
# Ejemplo
![[Pasted image 20261023184246.png]]
![[Pasted image 20261023184032.png]]
![[Pasted image 20261023184142.png]]![[Pasted image 20261023184156.png]]
![[Pasted image 20261023184231.png]]
# Transformacion iterativa a recursiva
original

```python
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
```

primera transformacion

```python
def principal_shell_sort_recursivo(lista):
	salto = len(lista)//2
	return shell_sort_recursivo(lista,salto)

def shell_sort_recursivo(lista, salto):
	n = len(lista) #constante
	if not salto > 0:
		return lista
	i = salto #variable dependiente
	while i <n:
		temp = lista[i] #constante dependiente
		j=i #variable dependiente
		while j >= salto and lista[j - salto]> temp:
			lista[j] = lista[j-salto]
			j -= salto #modificacion
		lista[j] = temp
		i+=1 #modificacion
	lista = shell_sort_recursivo(lista, salto//2)
```

segunda transformacion
```python
def aux(lista,salto,i):
	if i < n:
		temp = lista[i] #constante dependiente
		j=i #variable dependiente
		while j >= salto and lista[j - salto]> temp:
			lista[j] = lista[j-salto]
			j -= salto #modificacion
		lista[j] = temp
		lista = aux(lista,salto,i+1)
	return lista

def shell_sort_recursivo(lista, salto):
	n = len(lista) #constante
	if not salto > 0:
		return lista
	i = salto #variable dependiente
	if i <n:
		lista = aux(lista,salto,i)
	lista = shell_sort_recursivo(lista, salto//2)
```

tercera transformacion

```python
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

def shell_sort_recursivo(lista, salto):
	n = len(lista) #constante
	if not salto > 0:
		return lista
	i = salto #variable dependiente
	if i <n:
		lista = aux(lista,salto,i)
	lista = shell_sort_recursivo(lista, salto//2)
```