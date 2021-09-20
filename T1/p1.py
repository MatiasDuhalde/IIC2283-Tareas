"""
Solución a problema 1:
Dado un número N entero positivo, entregar la cantidad de caminos que pasan
por N aristas, en el multigrafo que representa al problema de los siete puentes
de Königsberg.
"""

# //////////
# CONSTANTES
# //////////

# Grafo
GRAPH_MATRIX = [
    [0, 2, 1, 0],
    [2, 0, 1, 2],
    [1, 1, 0, 1],
    [0, 2, 1, 0],
]


def GET_IDENTITY_MATRIX():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


MATRIX_DIM = 4

# Módulo (10 ** 9 + 7)
MOD = 1000000007

# /////////
# FUNCIONES
# /////////


def sum_matrix(matrix):
    res = 0
    for row in matrix:
        for col in row:
            res += col
            res %= MOD
    return res


def matrix_modmult(a, b):
    res = GET_IDENTITY_MATRIX()
    for i in range(MATRIX_DIM):
        for j in range(MATRIX_DIM):
            for k in range(MATRIX_DIM):
                res[i][j] += (a[i][k] * b[k][j])
                res[i][j] %= MOD
    return res


# Source: https://en.wikipedia.org/wiki/Modular_exponentiation#Matrices
def matrix_modexp(matrix, b):
    if b == 0:
        return GET_IDENTITY_MATRIX()
    if b == 1:
        return matrix
    if b % 2 == 1:
        return matrix_modmult(matrix, matrix_modexp(matrix, b - 1))
    D = matrix_modexp(matrix, b // 2)
    return matrix_modmult(D, D)


if __name__ == "__main__":
    # Obtener N
    n_value = int(input("N: "))
    if n_value == 0:
        print(0)
    else:
        print(sum_matrix(matrix_modexp(GRAPH_MATRIX, n_value)) % MOD)
