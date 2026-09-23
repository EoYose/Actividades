El programa tiene como objetivo hacer pasar a un caballo por un tablero de ajedrez de dimensiones MxN sin que pase por la misma casilla 2 veces, hacer esto requiere intentar avanzar siguiendo una ruta cuando se pueda y cuando no, retroceder para probar otra. Esto es un problema de backTracking

# Marco Teorico
## BackTracking
Es una tecnica de busqueda de soluciones que consiste en construir la solucion paso a paso y retroceder cuando un camino no funciona.
## MxN
Se refiere a las dimenciones del tablero, siendo **M** la cantidad de filas y **N** la cantidad de columnas que tiene
## Bottom-Up (De abajo a arriba)
Es un enfoque en el cual las ideas y soluciones surgen desde lo escencial (base del problema) para solucionar el problema desde dentro con las soluciones creadas

# Construccion del algoritmo
## Analisis

El algoritmo se creo con un enfoque bottom-up por lo que es necesario entender que es lo que necesita hacer.
### Extraccion de ideas
	"El caballo de ajedrez debe moverse por todas las casillas de un 
	tablero sin pasar por la misma casilla 2 veces o mas"
Lo esencial es:
1. El caballo de ajedrez
2. el movimiento del caballo por el tablero
3. Pasar por todas las casillas del tablero
4. No pasar por la misma casilla 2 veces o mas
--------
1. Sabemos que un caballo de ajedrez se mueve en L y tiene el potencial de hacer 8 movimientos distintos

2. El movimiento del caballo por el tablero esta limitado por el tamaño de este

3. Pasar por todas las casillas del tablero significa tener por donde empezar, tener que moverse y registrar su movimiento y determinar cuando paso por todo el tablero

4. No pasar por la misma casilla 2 veces o mas plantea que no basta con que el caballo pase por todo el tablero, sino que tambien tiene una forma estricta de pasar por el, esto implica que la cantidad de movimientos hechos en un tablero MxN sera de M\*N

## Nivel 1
Se dan las herramientas base del algoritmo
### El caballo 
El caballo se mueve en L y tiene potencial de hacer 8 movimientos distintos.
Pero para decir que se mueve necesitamos un punto de referencia, como el tablero funciona con filas y columnas entonces su posición será medida con fila y columna
```python
def mover(posicion, direccion):
    fila, columna = posicion # (fila, columna)
    match direccion:
        case 1:
            fila -= 2
            columna += 1
        case 2:
            fila -= 1
            columna += 2
        case 3:
            fila += 1
            columna += 2
        case 4:
            fila += 2
            columna += 1
        case 5:
            fila += 2
            columna -= 1
        case 6:
            columna -= 2
            fila += 1
        case 7:
            columna -= 2
            fila -= 1
        case 8:
            fila -= 2
            columna -= 1
    return (fila, columna)
```

### El movimiento del caballo por el tablero
El movimiento del caballo por el tablero esta limitado por el tamaño de este.
Asi que es necesario confirmar que el caballo este dentro del tablero, esto se verifica con su posicion y las dimensiones MxN del tablero.

La fila y columna no puede ser menor a la primera ni mayor a la ultima
la primera fila o columna es notada con un 0 por lo que la ultima no puede ser igual o mayor a M o N
```python
def dentro_tablero(pos,m,n):
    fila, columna = pos
    if not 0 <= fila < m:
        return False
    if not 0 <= columna < n:
        return False
    return True
```

### Pasar por todas las casillas del tablero
Pasar por todas las casillas del tablero significa tener un tablero por el cual pasar, un tablero es una matriz, así que se necesita una forma de crear una
```python
#Crea una matriz nula de MxN
def matriz_nula(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz
```
una vez teniendo una matriz, se puede decir que esta matriz es el tablero.
```python
tablero = matriz_nula(m,n)
```
es nula (llena de 0's) ya que no hay presencia del caballo en ella.
Pero el caballo necesita un lugar desde el cual empezar, normalmente se empieza desde el punto de origen (0,0) por lo que
```python
tablero[0][0] = 1
```
Para determinar si el caballo paso por todo el tablero se debe verificar que cada casilla del tablero haya sido marcada por el pasar del caballo, sin embargo el problema requiere que el caballo no pase por la misma casilla 2 veces o mas, por lo que esta solucion no puede darse sin antes entender el siguiente punto
### No pasar por la misma casilla 2 veces o mas
No pasar por la misma casilla 2 veces o mas requiere verificar que la posicion del caballo no este en un lugar del tablero en el que ya estuvo
```python
def movimiento_hecho(pos,tablero):
    fila, columna = pos
    return tablero[fila][columna] != 0
```
esto significa que hay que marcar el lugar por donde pasa el caballo, siendo conteo el contador de cuantos movimientos lleva hecho el caballo, de ahi es viene la necesidad de tener el tablero marcado con 0's con ``matriz_nula()``, para distinguir entre un 0 por el cual el caballo no paso y lo contrario a ello.
```python
tablero[fil][col] = conteo
```
y cada movimiento que haga el caballo se cuenta asi que
```python
conteo += 1
```
y como no se pueden repetir casillas, entonces la cantidad de movimientos sera el producto de M por N
entonces para saber si el caballo paso por todo el tablero
```python
if m*n == conteo:
    return True
```
## Nivel 2
Se dan las herramientas en las que ya se empieza a trabajar con el algoritmo

### Avanzar

```python
#Da los movimientos disponibles
disponibles = movimientos_disponibles(historial_posiciones[-1], tablero)

f, c = historial_posiciones[-1] #fila, columna
#Movimiento valido?
if candidato in disponibles and 8 >= candidato > aux[f][c]:
	conteo += 1

	#Anotar movimiento en aux
	fil, col = historial_posiciones[-1] #fila, columna
	aux[fil][col] = candidato

	#Oficializar movimiento 
	historial_posiciones.append(mover(historial_posiciones[-1], candidato))
	fil, col = historial_posiciones[-1] #fila, columna
	tablero[fil][col] = conteo
	
	candidato = 1

else:
	#Intentar con el siguiente movimiento
	candidato += 1
```
Avanzar dentro del tablero requiere conocer los movimientos disponibles para hacerse dentro de el.
Para eso se prueba cada combinacion de movimiento desde la posicion actual del caballo y se verifican para añadirse a la lista de movimientos disponibles
```python
def movimientos_disponibles(pos,tablero):
    disponibles = []
    m,n = obtener_dimensiones(tablero)
    for combinacion in range(1,9):
        intento = mover(pos,combinacion)
        if not dentro_tablero(intento,m,n):
            continue
        if movimiento_hecho(intento, tablero):
            continue
        disponibles.append(combinacion)
    return disponibles

def obtener_dimensiones(matriz:list):
    m = len(matriz)
    n = []
    for fila in matriz:
        if any(isinstance(x, int) for x in fila):
            n.append(len(fila))
        else:
            raise ValueError(f"Formato Invalido, solo numeros. {fila}")
    if len(n) == n.count(n[0]):
        n = n[0]
        return m,n
    else:
        raise ValueError(f"Matriz con dimensiones irregulares, matriz con {m} filas y {n} columnas")
```
cuando se verifica que el candidato esta entre los disponibles se realiza el movimiento con
```python
historial_posiciones.append(mover(historial_posiciones[-1], candidato))
fil, col = historial_posiciones[-1] #fila, columna
tablero[fil][col] = conteo
```