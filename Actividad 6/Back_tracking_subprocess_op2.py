# Hecho por Yosef Urquieta
# Asignatura: Programacion Estructurada (T-1)(L-1)

from multiprocessing import Process, Queue
import time


# Movimientos posibles del caballo
MOVIMIENTOS = (
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1)
)


def matriz_nula(m, n):
    return [[0] * n for _ in range(m)]


def buscar(primer_movimiento, resultado, dimensiones):

    m, n = dimensiones
    total = m * n

    tablero = matriz_nula(m, n)
    aux = matriz_nula(m, n)

    # --------------------------------------------------
    # Precalcular destinos de cada casilla
    # --------------------------------------------------

    movimientos = [[[] for _ in range(n)] for _ in range(m)]

    for fila in range(m):
        for columna in range(n):

            lista = movimientos[fila][columna]

            for direccion, (df, dc) in enumerate(MOVIMIENTOS, 1):

                f = fila + df
                c = columna + dc

                if 0 <= f < m and 0 <= c < n:
                    lista.append((direccion, f, c))

    # --------------------------------------------------
    # Posición inicial
    # --------------------------------------------------

    tablero[0][0] = 1

    posiciones = [(0, 0)]

    # --------------------------------------------------
    # Primer movimiento
    # --------------------------------------------------

    direccion = primer_movimiento - 1

    df, dc = MOVIMIENTOS[direccion]

    f = df
    c = dc

    if not (0 <= f < m and 0 <= c < n):
        resultado.put((False, None, None))
        return

    tablero[f][c] = 2
    aux[0][0] = primer_movimiento

    posiciones.append((f, c))

    print(f"Proceso iniciado con movimiento {primer_movimiento}")

    # --------------------------------------------------
    # Backtracking
    # --------------------------------------------------

    indice = [0] * total
    conteo = 2

    while posiciones:

        # Solución encontrada
        if conteo == total:
            resultado.put((True, tablero, aux))
            return

        fila, columna = posiciones[-1]

        opciones = movimientos[fila][columna]
        i = indice[conteo - 1]

        encontrado = False

        # Buscar siguiente movimiento válido
        while i < len(opciones):

            direccion, nf, nc = opciones[i]
            i += 1

            if tablero[nf][nc] == 0:
                indice[conteo - 1] = i

                # Realizar movimiento
                conteo += 1

                tablero[nf][nc] = conteo
                aux[fila][columna] = direccion

                posiciones.append((nf, nc))

                # Empezamos desde el primer movimiento
                # para la nueva posición
                indice[conteo - 1] = 0

                encontrado = True
                break

        if encontrado:
            continue

        # --------------------------------------------------
        # No quedan movimientos: retroceder
        # --------------------------------------------------

        indice[conteo - 1] = 0

        # Si estamos en la posición inicial del recorrido
        if conteo == 2:
            resultado.put((False, None, None))
            return

        fila, columna = posiciones.pop()

        tablero[fila][columna] = 0

        conteo -= 1

        # Limpiar el movimiento que llevaba a esta casilla
        fila_anterior, columna_anterior = posiciones[-1]
        aux[fila_anterior][columna_anterior] = 0


if __name__ == "__main__":

    inicio = time.time()

    m, n = 9,9

    print("Buscando solucion...")

    resultado = Queue()

    procesos = [
        Process(
            target=buscar,
            args=(3, resultado, (m, n))
        ),
        Process(
            target=buscar,
            args=(4, resultado, (m, n))
        )
    ]

    for proceso in procesos:
        proceso.start()

    solucion = False
    tablero_solucion = None
    aux_solucion = None

    resultados_recibidos = 0

    while resultados_recibidos < len(procesos):

        solucion, tablero, aux = resultado.get()

        resultados_recibidos += 1

        if solucion:
            tablero_solucion = tablero
            aux_solucion = aux
            break

    # --------------------------------------------------
    # Terminar procesos
    # --------------------------------------------------

    for proceso in procesos:

        if proceso.is_alive():
            proceso.terminate()

        proceso.join()

    # --------------------------------------------------
    # Mostrar resultado
    # --------------------------------------------------

    if solucion:

        for fila in range(m):
            print(
                str(tablero_solucion[fila]) +
                str(aux_solucion[fila])
            )

    print("La existencia de la solucion es:", solucion)

    final = time.time()

    print(
        "Ha tardado",
        round(final - inicio, 3),
        "segundos"
    )