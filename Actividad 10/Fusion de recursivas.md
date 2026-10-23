
Funcion original
```python
#complemento
def aux(arreglo,j):
	n = len(arreglo)
	if arreglo[j] > arreglo[j+1]:
		arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
	if j < n-2:
		return aux(arreglo,j+1)
	return arreglo

#Ordenar arreglos (Ordenamiento de la burbuja)
def ordenar_recursivo_burbuja(arreglo, i):
	n = len(arreglo)
	if i<n:
		arreglo = aux(arreglo,0)
	if i<n-1:
		return ordenar_recursivo_burbuja(arreglo,i+1)
	return arreglo
```

Funcion fusionada

```python
def ordenar_recursivo_burbuja(arreglo, i=0, j=0):
    n = len(arreglo)

    if n < 2 or i >= n - 1:
        return arreglo

    if j < n - 1:
        if arreglo[j] > arreglo[j + 1]:
            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

        return ordenar_recursivo_burbuja(arreglo, i, j + 1)

    return ordenar_recursivo_burbuja(arreglo, i + 1, 0)
```