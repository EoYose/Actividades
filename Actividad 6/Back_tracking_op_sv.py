#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)

import json
import os
import time
import copy

#Devuelve las coordenadas correspondientes al destino
def mover(pos, direccion):
    fila, columna = pos
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

#Consulta si la posicion ya fue hecha
def movimiento_hecho(pos,tablero):
    fila, columna = pos
    return tablero[fila][columna] != 0

#Consulta si la posicion esta dentro del tablero
def dentro_tablero(pos,m,n):
    fila, columna = pos
    if not 0 <= fila < m:
        return False
    if not 0 <= columna < n:
        return False
    return True

#Obtiene las dimensiones del tablero
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

#Filtra los movimientos disponibles
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

#Verifica la condicion de termino del programa
#Tambien determina si el problema tiene solucion o no
def fin(dimensiones, historial_posiciones):
    m,n = dimensiones
    v = 0
    profundidad = len(historial_posiciones)
    if m*n == profundidad:
        return True
    if profundidad == 0:
        return False
    return None

#Crea una matriz nula de MxN
def matriz_nula(m,n):
    matriz = []
    for fila in range(m):
        aux = []
        for columna in range(n):
            aux.append(0)
        matriz.append(aux)
    return matriz

def guardar(estado_guardado):
    fin = time.time()
    m,n = obtener_dimensiones(estado_guardado["tablero"])
    file = open("SAVE.json", "r")
    datos = json.loads(file.read())
    MxN = datos.get(f"{m}x{n}")
    if MxN != None:
        tiempo = MxN.get("tiempo")
        if tiempo == None:
            tiempo = 0
        tiempo = round(tiempo+(fin-inicio),3)
    else:
        tiempo = round(fin-inicio,3)
    file.close()
    datos[f"{m}x{n}"] = {
    "dimensiones" : (m,n),
    "solucion" : estado_guardado["solucion"],
    "profundidad" : estado_guardado["profundidad"],
    "candidato" : estado_guardado["candidato"],
    "intentos" : estado_guardado["intentos"],
    "tiempo" : tiempo,
    "tablero" : estado_guardado["tablero"],
    "aux" : estado_guardado["aux"],
    "visitas" : estado_guardado["visitas"],
    "visitas_profundidad" : estado_guardado["visitas_profundidad"],
    "historial_posiciones" : estado_guardado["historial_posiciones"]
    }
    file = open("SAVE.json", "w")
    json.dump(datos, file,indent=2)
    file.close()

def preguntar_numero(text):
    while True:
        respuesta = input(text)
        if respuesta.isnumeric():
            numero = int(respuesta)
            return numero
        else:
            print("Por favor ingrese un numero")

if not os.path.isfile("SAVE.json"):
    print("Archivo de guardado no encontrado.")
    print("Creando uno nuevo")
    open("SAVE.json", "+w").write("{}")

file_save = False
menu = True
print("Desea empezar desde cero?")
respuesta = input("(s/n): ")
if "s" in respuesta.lower():
    menu = False

while menu:
    try:
        file = json.loads(open("SAVE.json", "r").read())
    except json.decoder.JSONDecodeError:
        open("SAVE.json", "+w").write("{}")
        file = json.loads(open("SAVE.json", "r").read())
    print("Escriba el tablero a buscar")
    print("Ejemplo: 5x5")
    print("Tableros disponibles: ")
    print("\n".join(file.keys()))
    try:
        respuesta = input("(MxN): ")
    except KeyboardInterrupt:
        print("Saliendo del menu...")
        break
    MxN = file.get(str(respuesta))
    if MxN == None:
        print("Direccion no encontrada, intententelo nuevamente")
        continue
    else:
        m,n = MxN["dimensiones"]
        tablero = MxN["tablero"]
        aux = MxN["aux"]
        profundidad = MxN["profundidad"]
        candidato = MxN["candidato"]
        historial_posiciones = MxN["historial_posiciones"]
        solucion = MxN["solucion"]
        intentos = MxN["intentos"]
        visitas = MxN["visitas"]
        visitas_profundidad = MxN.get("visitas_profundidad", [0 for _ in range(m*n)])
        fallo_profundidad = MxN.get("fallo_profundidad", [0 for _ in range(m*n)])
        file_save = True
        break


if file_save == False:
    print("Escriba las dimenciones del tablero MxN")
    m = preguntar_numero("M: ")
    n = preguntar_numero("N: ")

    #Verifica que no se este sobre escribiendo un tablero en proceso/solucionado
    file = json.loads(open("SAVE.json", "r").read())
    MxN = file.get(f"{m}x{n}")
    if MxN != None:
        print("Ya existe un tablero con las mismas dimensiones siendo resuelto")
        print("Desea sobre escribirlo?")
        respuesta = input("(s/n): ")
        if "s" in respuesta.lower():
            pass
        else:
            print("accion abortada")
            exit()
    
    #Indica las posiciones por las que ha estado el caballo
    tablero = matriz_nula(m,n)
    #Empieza desde (0,0)
    tablero[0][0] = 1
    #Indica los movimientos que ha realizado el caballo en cada posicion
    aux = matriz_nula(m,n)
    #Registra cuantas veces se ha pasado por una misma casilla
    #Permite tener registro de las zonas mas costosas computacionalmente
    visitas = matriz_nula(m,n)
    #Registra cuantas veces se ha entrado a una profundidad
    visitas_profundidad = [0 for _ in range(m*n)]
    #Registra cuantas veces se ha salido de una profundidad
    fallo_profundidad = [0 for _ in range(m*n)]
    


    solucion = None
    profundidad = 1
    candidato = 0
    historial_posiciones = [(0,0)]
    intentos = 0
    retrocesos = 0
auxiliar_de_optimizacion = 0
print("Buscando solucion")
inicio = time.time()
solucion = fin((m,n), historial_posiciones)
if solucion != None:
    print("La solucion ya fue determinada previamente")
try:
    while solucion == None:
        auxiliar_de_optimizacion += 1

        #Da los movimientos disponibles
        disponibles = movimientos_disponibles(historial_posiciones[-1], tablero)

        #Sin movimientos?
        if candidato >= len(disponibles):
            #El candidato se vuele 0 ya que se empieza desde la direccion 0 en la lista de disponibilidad
            candidato = 0

            #Deshacer movimiento
            f,c = historial_posiciones[-1]
            tablero[f][c] = 0
            aux[f][c] = 0
            del historial_posiciones[-1]
            profundidad = len(historial_posiciones)
            continue

        f, c = historial_posiciones[-1] #fila, columna
        #Movimiento valido?
        if not 8 >= disponibles[candidato] > aux[f][c]:
            #Intentar con el siguiente movimiento
            candidato += 1
            continue

        #Se realizo una optimizacion en la que en vez de ir de 1 a 8 candidato por candidato
        #Se va desde candidato 0 hasta len(disponibles), saltandose automaticamente los no disponibles
        #el sistema se adapta al caso de no tener ninguna disponible con la condicional de esta sangria
        #contador de intentos de avances
        intentos += 1

        fil, col = historial_posiciones[-1] #fila, columna
        #Anotar movimiento en aux
        aux[fil][col] = disponibles[candidato]
        #Anotar visita
        visitas[fil][col] += 1
        profundidad = len(historial_posiciones)
        visitas_profundidad[profundidad-1] += 1

        #Oficializar movimiento 
        historial_posiciones.append(mover(historial_posiciones[-1], disponibles[candidato]))
        fil, col = historial_posiciones[-1] #fila, columna
        tablero[fil][col] = len(historial_posiciones)
        
        candidato = 0
        solucion = fin((m,n), historial_posiciones)

        if auxiliar_de_optimizacion >= 22000:
            auxiliar_de_optimizacion = 0
            estado_guardado = {
            "solucion": copy.deepcopy(solucion),
            "intentos": copy.deepcopy(intentos),
            "inicio": copy.deepcopy(inicio),
            "profundidad": copy.deepcopy(profundidad),
            "candidato": copy.deepcopy(candidato),
            "tablero": copy.deepcopy(tablero),
            "aux": copy.deepcopy(aux),
            "visitas": copy.deepcopy(visitas),
            "visitas_profundidad": copy.deepcopy(visitas_profundidad),
            "historial_posiciones": copy.deepcopy(historial_posiciones),
            }

except KeyboardInterrupt:
    #Guarda si se interrumpe el proceso con ctrl+c
    guardar(estado_guardado)
    exit()


#Muestra el tablero final
print(f"\n".join([str([str(i) for i in tablero][x]) + str([str(e) for e in aux][x]) for x in range(m)])) # Muestra el tablero y el tablero auxiliar
print("La existencia de la solucion es:", solucion)


guardar(estado_guardado)

input("Presione enter para salir")
