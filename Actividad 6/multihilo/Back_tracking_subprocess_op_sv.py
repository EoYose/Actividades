#Hecho por Yosef Urquieta
#Asignatura: Programacion Estructurada (T-1)(L-1)

import json
import os
import copy
from multiprocessing import Process, Queue, Event


# ============================================================
# MOVIMIENTOS
# ============================================================

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
def movimiento_hecho(pos, tablero):
    fila, columna = pos
    return tablero[fila][columna] != 0


#Consulta si la posicion esta dentro del tablero
def dentro_tablero(pos, m, n):
    fila, columna = pos

    if not 0 <= fila < m:
        return False

    if not 0 <= columna < n:
        return False

    return True


#Obtiene las dimensiones del tablero
def obtener_dimensiones(matriz: list):
    m = len(matriz)
    n = []

    for fila in matriz:
        if any(isinstance(x, int) for x in fila):
            n.append(len(fila))
        else:
            raise ValueError(
                f"Formato Invalido, solo numeros. {fila}"
            )

    if len(n) == n.count(n[0]):
        n = n[0]
        return m, n
    else:
        raise ValueError(
            f"Matriz con dimensiones irregulares, "
            f"matriz con {m} filas y {n} columnas"
        )


#Filtra los movimientos disponibles
def movimientos_disponibles(pos, tablero):
    disponibles = []

    m, n = obtener_dimensiones(tablero)

    for combinacion in range(1, 9):

        intento = mover(pos, combinacion)

        if not dentro_tablero(intento, m, n):
            continue

        if movimiento_hecho(intento, tablero):
            continue

        disponibles.append(combinacion)

    return disponibles


# ============================================================
# CONDICION DE TERMINO
# ============================================================

#Verifica la condicion de termino del programa
def fin(dimensiones, conteo, historial_posiciones):

    m, n = dimensiones

    if m * n == conteo:
        return True

    else:
        if len(historial_posiciones) == 0:
            return False

    return None


# ============================================================
# MATRICES
# ============================================================

#Crea una matriz nula de MxN
def matriz_nula(m, n):

    matriz = []

    for fila in range(m):

        aux = []

        for columna in range(n):
            aux.append(0)

        matriz.append(aux)

    return matriz


# ============================================================
# GUARDADO
# ============================================================

def guardar(
    tablero,
    aux,
    solucion,
    historial_posiciones,
    conteo,
    candidato,
    visitas,
    intentos,
    retrocesos
):

    m, n = obtener_dimensiones(tablero)

    with open("SAVE.json", "r") as file:
        datos = json.load(file)

    datos[f"{m}x{n}"] = {
        "dimensiones": (m, n),
        "solucion": solucion,
        "conteo": conteo,
        "candidato": candidato,
        "intentos": intentos,
        "retrocesos": retrocesos,
        "tablero": tablero,
        "aux": aux,
        "visitas": visitas,
        "historial_posiciones": historial_posiciones
    }

    with open("SAVE.json", "w") as file:
        json.dump(datos, file, indent=2)


# ============================================================
# ENTRADA
# ============================================================

def preguntar_numero(text):

    while True:

        respuesta = input(text)

        if respuesta.isnumeric():
            numero = int(respuesta)
            return numero

        else:
            print("Por favor ingrese un numero")


# ============================================================
# BACKTRACKING
# ============================================================

def buscar(estado, cola, evento_solucion):

    tablero = estado["tablero"]
    aux = estado["aux"]
    visitas = estado["visitas"]

    conteo = estado["conteo"]
    candidato = estado["candidato"]
    historial_posiciones = estado["historial_posiciones"]

    intentos = 0
    retrocesos = 0

    m, n = obtener_dimensiones(tablero)

    solucion = fin(
        (m, n),
        conteo,
        historial_posiciones
    )

    while solucion is None:

        #Si otro proceso encontro una solucion,
        #este proceso puede detenerse.
        if evento_solucion.is_set():
            break

        disponibles = movimientos_disponibles(
            historial_posiciones[-1],
            tablero
        )

        f, c = historial_posiciones[-1]

        # ----------------------------------------------------
        # INTENTAR MOVIMIENTO
        # ----------------------------------------------------

        if (
            len(disponibles) != 0
            and candidato < len(disponibles)
            and disponibles[candidato] > aux[f][c]
        ):

            movimiento = disponibles[candidato]

            conteo += 1
            intentos += 1

            #Registrar candidato probado
            aux[f][c] = movimiento

            #Registrar visita
            visitas[f][c] += 1

            #Realizar movimiento
            nueva_posicion = mover(
                historial_posiciones[-1],
                movimiento
            )

            historial_posiciones.append(
                nueva_posicion
            )

            fil, col = nueva_posicion

            tablero[fil][col] = conteo

            #Comenzar nuevamente desde el primer
            #movimiento disponible de la nueva casilla
            candidato = 0

        else:

            #Probar siguiente candidato
            candidato += 1

        # ----------------------------------------------------
        # SIN MOVIMIENTOS -> BACKTRACKING
        # ----------------------------------------------------

        if candidato >= len(disponibles):

            candidato = 0

            retrocesos += 1

            #No intentar borrar la posicion inicial
            if len(historial_posiciones) <= 1:

                solucion = False
                break

            #Deshacer ultima posicion
            f, c = historial_posiciones[-1]

            tablero[f][c] = 0
            aux[f][c] = 0

            historial_posiciones.pop()

            conteo -= 1

        solucion = fin(
            (m, n),
            conteo,
            historial_posiciones
        )

    # --------------------------------------------------------
    # RESULTADO DEL PROCESO
    # --------------------------------------------------------

    resultado = {
        "tablero": tablero,
        "aux": aux,
        "visitas": visitas,
        "historial_posiciones": historial_posiciones,
        "conteo": conteo,
        "candidato": candidato,
        "intentos": intentos,
        "retrocesos": retrocesos,
        "solucion": solucion
    }

    cola.put(resultado)

    #Si realmente encontro una solucion,
    #avisa al proceso principal y al otro proceso.
    if solucion is True:
        evento_solucion.set()


# ============================================================
# CREACION DE RAMAS
# ============================================================

def crear_estado_inicial(
    tablero,
    aux,
    visitas,
    historial_posiciones,
    movimiento
):

    tablero = copy.deepcopy(tablero)
    aux = copy.deepcopy(aux)
    visitas = copy.deepcopy(visitas)
    historial_posiciones = copy.deepcopy(
        historial_posiciones
    )

    #La casilla actual es (0,0)
    aux[0][0] = movimiento
    visitas[0][0] += 1

    #Realizar primer movimiento
    nueva_posicion = mover(
        (0, 0),
        movimiento
    )

    historial_posiciones.append(
        nueva_posicion
    )

    #La primera casilla ya era 1
    #por lo tanto esta es la casilla 2
    fil, col = nueva_posicion

    tablero[fil][col] = 2

    return {
        "tablero": tablero,
        "aux": aux,
        "visitas": visitas,
        "conteo": 2,
        "candidato": 0,
        "historial_posiciones": historial_posiciones
    }

if __name__ == "__main__":
    # ============================================================
    # INICIO DEL PROGRAMA
    # ============================================================

    if not os.path.isfile("SAVE.json"):

        print("Archivo de guardado no encontrado.")
        print("Creando uno nuevo.")

        with open("SAVE.json", "w") as file:
            file.write("{}")


    file_save = False
    menu = True

    print("Desea empezar desde cero?")
    respuesta = input("(s/n): ")

    if "s" in respuesta.lower():
        menu = False


    # ============================================================
    # CARGAR GUARDADO
    # ============================================================

    while menu:

        try:

            with open("SAVE.json", "r") as file:
                file = json.load(file)

        except json.decoder.JSONDecodeError:

            with open("SAVE.json", "w") as file:
                file.write("{}")

            with open("SAVE.json", "r") as file:
                file = json.load(file)

        print("Escriba el tablero a buscar")
        print("Ejemplo: 5x5")

        print("Tableros disponibles:")
        print("\n".join(file.keys()))

        try:
            respuesta = input("(MxN): ")

        except KeyboardInterrupt:

            print("Saliendo del menu...")
            exit()

        MxN = file.get(str(respuesta))

        if MxN is None:

            print(
                "Direccion no encontrada, "
                "intententelo nuevamente"
            )

            continue

        else:

            m, n = MxN["dimensiones"]

            tablero = MxN["tablero"]
            aux = MxN["aux"]
            conteo = MxN["conteo"]
            candidato = MxN["candidato"]

            historial_posiciones = MxN[
                "historial_posiciones"
            ]

            solucion = MxN["solucion"]

            intentos = MxN["intentos"]
            retrocesos = MxN["retrocesos"]

            visitas = MxN["visitas"]

            file_save = True

            break


    # ============================================================
    # CREAR TABLERO NUEVO
    # ============================================================

    if file_save == False:

        print("Escriba las dimenciones del tablero MxN")

        m = preguntar_numero("M: ")
        n = preguntar_numero("N: ")

        #Verifica si ya existe
        with open("SAVE.json", "r") as file:
            datos = json.load(file)

        MxN = datos.get(f"{m}x{n}")

        if MxN is not None:

            print(
                "Ya existe un tablero con las mismas "
                "dimensiones siendo resuelto"
            )

            print("Desea sobre escribirlo?")

            respuesta = input("(s/n): ")

            if "s" not in respuesta.lower():

                print("accion abortada")
                exit()

        #Crear tablero
        tablero = matriz_nula(m, n)

        #Empieza desde (0,0)
        tablero[0][0] = 1

        #Candidatos utilizados
        aux = matriz_nula(m, n)

        #Visitas por casilla
        visitas = matriz_nula(m, n)

        solucion = None
        conteo = 1
        candidato = 0

        historial_posiciones = [
            (0, 0)
        ]

        intentos = 0
        retrocesos = 0


    # ============================================================
    # BUSQUEDA
    # ============================================================

    print("\nBuscando solucion con 2 procesos...")
    print("CPU principal: proceso coordinador")
    print("CPU 1: rama inicial")
    print("CPU 2: rama inicial")


    # ------------------------------------------------------------
    # Si ya existe una solucion guardada
    # ------------------------------------------------------------

    if solucion is not None:

        print(
            "La solucion ya fue determinada previamente."
        )


    else:

        # --------------------------------------------------------
        # Obtener ramas iniciales
        # --------------------------------------------------------

        disponibles = movimientos_disponibles(
            historial_posiciones[-1],
            tablero
        )

        #Para un tablero 9x9 desde (0,0)
        #normalmente seran las direcciones 3 y 4.
        if len(disponibles) == 0:

            solucion = False

        else:

            #Evento compartido entre procesos.
            evento_solucion = Event()

            procesos = []
            colas = []

            # ----------------------------------------------------
            # Crear un proceso por cada movimiento inicial.
            #
            # En 9x9 desde (0,0) son normalmente 2 procesos.
            # ----------------------------------------------------

            for movimiento in disponibles[:2]:

                estado = crear_estado_inicial(
                    tablero,
                    aux,
                    visitas,
                    historial_posiciones,
                    movimiento
                )

                cola = Queue()

                proceso = Process(
                    target=buscar,
                    args=(
                        estado,
                        cola,
                        evento_solucion
                    )
                )

                procesos.append(proceso)
                colas.append(cola)

            # ----------------------------------------------------
            # Iniciar procesos
            # ----------------------------------------------------

            for proceso in procesos:
                proceso.start()

            resultados = []

            # ----------------------------------------------------
            # Esperar resultados
            # ----------------------------------------------------

            try:

                for cola in colas:

                    resultado = cola.get()

                    resultados.append(
                        resultado
                    )

            except KeyboardInterrupt:

                print("\nInterrupcion detectada.")
                print("Terminando procesos...")

                for proceso in procesos:

                    if proceso.is_alive():
                        proceso.terminate()

                for proceso in procesos:
                    proceso.join()

                print("Procesos terminados.")
                exit()

            # ----------------------------------------------------
            # Esperar que terminen los procesos
            # ----------------------------------------------------

            for proceso in procesos:
                proceso.join()

            # ----------------------------------------------------
            # Mostrar estadisticas de cada rama
            # ----------------------------------------------------

            print("\n========== RESULTADOS ==========")

            for i, resultado in enumerate(resultados):

                print(
                    f"\nProceso {i + 1}"
                )

                print(
                    f"Conteo final: "
                    f"{resultado['conteo']}"
                )

                print(
                    f"Intentos: "
                    f"{resultado['intentos']}"
                )

                print(
                    f"Retrocesos: "
                    f"{resultado['retrocesos']}"
                )

                print(
                    f"Solucion: "
                    f"{resultado['solucion']}"
                )

            # ----------------------------------------------------
            # Elegir resultado
            # ----------------------------------------------------

            #Si alguno encontro solucion,
            #nos quedamos con ella.
            soluciones = [
                r for r in resultados
                if r["solucion"] is True
            ]

            if len(soluciones) > 0:

                resultado_final = max(
                    soluciones,
                    key=lambda r: r["conteo"]
                )

            else:

                #Si ninguno encontro solucion,
                #conservar la rama que llego mas lejos.
                resultado_final = max(
                    resultados,
                    key=lambda r: r["conteo"]
                )

            # ----------------------------------------------------
            # Copiar resultado final
            # ----------------------------------------------------

            tablero = resultado_final["tablero"]
            aux = resultado_final["aux"]
            visitas = resultado_final["visitas"]

            historial_posiciones = (
                resultado_final["historial_posiciones"]
            )

            conteo = resultado_final["conteo"]
            candidato = resultado_final["candidato"]

            intentos = resultado_final["intentos"]
            retrocesos = resultado_final["retrocesos"]

            solucion = resultado_final["solucion"]


    # ============================================================
    # RESULTADO FINAL
    # ============================================================

    print("\n========== RESULTADO FINAL ==========")

    print(
        "\n".join(
            [
                str(
                    [str(i) for i in tablero][x]
                )
                +
                str(
                    [str(e) for e in aux][x]
                )
                for x in range(m)
            ]
        )
    )

    print(
        "\nLa existencia de la solucion es:",
        solucion
    )

    print(
        "Conteo:",
        conteo
    )

    print(
        "Intentos:",
        intentos
    )

    print(
        "Retrocesos:",
        retrocesos
    )


    # ============================================================
    # GUARDAR
    # ============================================================

    guardar(
        tablero=tablero,
        aux=aux,
        conteo=conteo,
        candidato=candidato,
        solucion=solucion,
        historial_posiciones=historial_posiciones,
        visitas=visitas,
        intentos=intentos,
        retrocesos=retrocesos
    )


    input("\nPresione enter para salir")