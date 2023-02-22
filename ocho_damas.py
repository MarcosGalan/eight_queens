import copy

tablero = [
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_']
]


def bloqueo_posiciones(tablero, pos_reina):
    for pos, row in enumerate(tablero):
        if tablero[pos][pos_reina[0]] != 'o':
            tablero[pos][pos_reina[0]] = 'x'

    for pos, element in enumerate(tablero[pos_reina[1]]):
        if element != "o":
            tablero[pos_reina[1]][pos] = "x"

    diagonal_ud = (pos_reina[0] - pos_reina[1], 0) if pos_reina[0] > pos_reina[1] else (0, pos_reina[1] - pos_reina[0])
    diagonal_du = (pos_reina[0] - ((len(tablero) - 1) - pos_reina[1]), (len(tablero) - 1)) if pos_reina[0] > (
            (len(tablero) - 1) - pos_reina[1]) else (0, pos_reina[1] + pos_reina[0])

    stop = False
    while not stop:
        stop = True
        if diagonal_ud[0] >= len(tablero[0]) or diagonal_ud[1] >= len(tablero):
            pass
        else:
            tablero[diagonal_ud[1]][diagonal_ud[0]] = 'x' if tablero[diagonal_ud[1]][diagonal_ud[0]] != 'o' else 'o'
            diagonal_ud = list(map(lambda x: x + 1, diagonal_ud))
            stop = stop * False
        if diagonal_du[0] >= len(tablero[0]) or diagonal_du[1] < 0:
            pass
        else:
            tablero[diagonal_du[1]][diagonal_du[0]] = 'x' if tablero[diagonal_du[1]][diagonal_du[0]] != 'o' else 'o'
            diagonal_du = (diagonal_du[0] + 1, diagonal_du[1] - 1)
            stop = stop * False

    tablero[pos_reina[1]][pos_reina[0]] = 'o'

    return tablero


def ocho_reinas(tablero_local):
    completo = True
    dama_count = 0
    for i in tablero_local:
        for j in i:
            if j == '_':
                completo = completo * False

            if j == 'o':
                dama_count += 1

    if dama_count == 8:
        return tablero_local

    if completo:
        return None

    for pos_fila, fila in enumerate(tablero_local):
        for pos_element, elemento in enumerate(fila):
            if elemento == '_':
                tablero_temporal = bloqueo_posiciones(copy.deepcopy(tablero_local), (pos_element, pos_fila))
                res = ocho_reinas(tablero_temporal)
                if res is not None:
                    return res

