from rich import print
import copy

tablero = [
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']]


def bloqueo_posiciones(tablero_loc, pos_reina) -> list:
    tablero_loc_temp = copy.deepcopy(tablero_loc)
    for pos, i in enumerate(tablero_loc_temp[pos_reina[0]]):
        if i != 'o':
            tablero_loc_temp[pos_reina[0]][pos] = 'x'

    for pos, j in enumerate(tablero_loc_temp):
        if j[pos_reina[1]] != 'o':
            tablero_loc_temp[pos][pos_reina[1]] = 'x'

    diagonal_id = list(pos_reina)
    diagonal_di = list(pos_reina)

    while True:
        if diagonal_id[0] == 0 or diagonal_id[1] == 0:
            break
        diagonal_id[0] -= 1
        diagonal_id[1] -= 1

    while diagonal_di[0] != 0 or diagonal_di[1] != 0:
        diagonal_di[0] += 1
        diagonal_di[1] -= 1
        if diagonal_id[0] == 0 or diagonal_id[1] == 0:
            break

    while True:
        try:
            if tablero_loc_temp[diagonal_id[0]][diagonal_id[1]] != 'o':
                tablero_loc_temp[diagonal_id[0]][diagonal_id[1]] = 'x'
            diagonal_id[0] += 1
            diagonal_id[1] += 1
        except IndexError:
            break
    while True:
        try:

            if tablero_loc_temp[diagonal_di[0]][diagonal_di[1]] != 'o':
                tablero_loc_temp[diagonal_di[0]][diagonal_di[1]] = 'x'
            if diagonal_di[0] <= 0:
                break
            diagonal_di[0] -= 1
            diagonal_di[1] += 1
        except IndexError:
            break

    return tablero_loc_temp


def ocho_reinas(tablero_local, n_dama=1):
    print('cargando')
    completo = True
    dama_count = 0
    for i in tablero_local:
        for j in i:
            if j == '':
                completo = completo * False

            if j == 'o':
                dama_count += 1

    if dama_count == 8:
        return tablero_local

    if completo:
        return None

    for pos_fila, fila in enumerate(tablero_local):
        for pos_element, elemento in enumerate(fila):
            tablero_temporal = copy.deepcopy(tablero_local)
            if elemento == '':
                tablero_temporal[pos_fila][pos_element] = 'o'
                tablero_temporal = bloqueo_posiciones(tablero_temporal, (pos_fila, pos_element))
                res = ocho_reinas(tablero_temporal, n_dama + 1)
                if res is not None:
                    return res


