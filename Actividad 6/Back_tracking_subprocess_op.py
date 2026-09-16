# Hecho por Yosef Urquieta
# Asignatura: Programacion Estructurada (T-1)(L-1)

from multiprocessing import Process, Queue
import time


# Devuelve las coordenadas correspondientes al destino
def mover(pos, direccion):
    fila, columna = pos

    movimientos = (
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1)
    )

    df, dc = movimientos[direccion - 1]

    return fila + df, columna + dc


# Crea una matriz nula de MxN
def matriz_nula(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]


# Filtra los movimientos disponibles
def movimientos_disponibles(pos, tablero, movimientos):
    disponibles = []

    for direccion, destino in movimientos[pos]:
        fila, columna = destino

        if tablero[fila][columna] == 0:
            disponibles.append(direccion)

    return disponibles


# Realiza la búsqueda mediante backtracking
def buscar(primer_movimiento, resultado, dimensiones):

    m, n = dimensiones

    tablero = matriz_nula(m, n)
    aux = matriz_nula(m, n)

    tablero[0][0] = 1

    conteo = 1

    historial_posiciones = [(0, 0)]

    # --------------------------------------------------
    # Precalcular movimientos válidos de cada casilla
    # --------------------------------------------------

    movimientos = {}

    for fila in range(m):
        for columna in range(n):

            pos = (fila, columna)
            movimientos[pos] = []

            for direccion in range(1, 9):

                destino = mover(pos, direccion)

                f, c = destino

                if 0 <= f < m and 0 <= c < n:
                    movimientos[pos].append(
                        (direccion, destino)
                    )

    # --------------------------------------------------
    # Primer movimiento
    # --------------------------------------------------

    conteo += 1

    fil, col = historial_posiciones[-1]

    aux[fil][col] = primer_movimiento

    siguiente = mover(
        historial_posiciones[-1],
        primer_movimiento
    )

    historial_posiciones.append(siguiente)

    fil, col = siguiente

    # Si el primer movimiento no es válido
    if not (0 <= fil < m and 0 <= col < n):
        resultado.put((False, None, None))
        return

    tablero[fil][col] = conteo

    print(f"Proceso iniciado con movimiento {primer_movimiento}")

    candidato = 0

    while True:

        # ----------------------------------------------
        # ¿Ya llenamos el tablero?
        # ----------------------------------------------

        if conteo == m * n:
            resultado.put((True, tablero, aux))
            return

        # ----------------------------------------------
        # Movimientos posibles
        # ----------------------------------------------

        posicion_actual = historial_posiciones[-1]

        disponibles = movimientos_disponibles(
            posicion_actual,
            tablero,
            movimientos
        )

        f, c = posicion_actual

        # ----------------------------------------------
        # Intentar movimiento
        # ----------------------------------------------

        if (
            candidato < len(disponibles)
            and disponibles[candidato] > aux[f][c]
        ):

            direccion = disponibles[candidato]

            conteo += 1

            aux[f][c] = direccion

            siguiente = mover(
                posicion_actual,
                direccion
            )

            historial_posiciones.append(siguiente)

            fil, col = siguiente

            tablero[fil][col] = conteo

            candidato = 0

        else:

            candidato += 1

        # ----------------------------------------------
        # No quedan movimientos
        # ----------------------------------------------

        if candidato >= len(disponibles):

            candidato = 0

            # Llegamos al inicio de la búsqueda
            if len(historial_posiciones) == 1:
                resultado.put((False, None, None))
                return

            conteo -= 1

            f, c = historial_posiciones[-1]

            tablero[f][c] = 0
            aux[f][c] = 0

            del historial_posiciones[-1]


if __name__ == "__main__":

    inicio = time.time()

    m, n = 9,9

    print("Buscando solucion...")

    resultado = Queue()

    proceso_1 = Process(
        target=buscar,
        args=(3, resultado, (m, n))
    )

    proceso_2 = Process(
        target=buscar,
        args=(4, resultado, (m, n))
    )

    proceso_1.start()
    proceso_2.start()

    solucion = None
    tablero_solucion = None
    aux_solucion = None

    resultados_recibidos = 0

    while resultados_recibidos < 2:

        solucion, tablero, aux = resultado.get()

        resultados_recibidos += 1

        if solucion is True:

            tablero_solucion = tablero
            aux_solucion = aux

            break

    # Terminar procesos restantes

    if proceso_1.is_alive():
        proceso_1.terminate()

    if proceso_2.is_alive():
        proceso_2.terminate()

    proceso_1.join()
    proceso_2.join()

    # Mostrar resultado

    if solucion:

        for x in range(m):
            print(
                str(tablero_solucion[x]) +
                str(aux_solucion[x])
            )

    print("La existencia de la solucion es:", solucion)

    final = time.time()

    print(
        "Ha tardado",
        round(final - inicio, 3),
        "segundos"
    )