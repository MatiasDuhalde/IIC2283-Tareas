"""
Solución a problema 1:
Dado un número N entero positivo, entregar la cantidad de caminos que pasan
por N aristas, en el multigrafo que representa al problema de los siete puentes
de Königsberg.
"""

# //////////
# CONSTANTES
# //////////

# Grafo (representando puentes de Königsberg)
GRAPH_MATRIX = [
    [0, 2, 1, 0],
    [2, 0, 1, 2],
    [1, 1, 0, 1],
    [0, 2, 1, 0],
]


def GET_IDENTITY_MATRIX():
    """
    Obtener matriz identidad (dimensiones fijas para este problema)
    """
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


# Dimensión de la matriz
MATRIX_DIM = 4

# Módulo (10 ** 9 + 7)
MOD = 1000000007

# /////////
# FUNCIONES
# /////////


def sum_matrix(matrix):
    """
    Suma todos los elementos de una matriz, calculando el módulo
    Complejidad fija para dimensión = 4
    --> O(1)
    """
    res = 0
    for row in matrix:
        for col in row:
            res += col
            res %= MOD
    return res


def matrix_modmult(a, b):
    """
    Producto matricial de dos matrices, calculando el módulo
    Complejidad fija para dimensión = 4
    --> O(1)
    """
    res = GET_IDENTITY_MATRIX()
    for i in range(MATRIX_DIM):
        for j in range(MATRIX_DIM):
            for k in range(MATRIX_DIM):
                res[i][j] += (a[i][k] * b[k][j])
                res[i][j] %= MOD
    return res


# Source: https://en.wikipedia.org/wiki/Modular_exponentiation#Matrices
def matrix_modexp(matrix, b):
    """
    Exponenciación modular de una matriz
    Complejidad dependiente de b
    --> O(log2(b))
    """
    if b == 0:
        # Caso base, constante
        return GET_IDENTITY_MATRIX()
    if b == 1:
        # Caso base, constante
        return matrix
    if b % 2 == 1:
        # Producto matricial es constante para dimensiones fijas -> O(1)
        # Recursión de matrix_modexp, + b
        return matrix_modmult(matrix, matrix_modexp(matrix, b - 1))
    # Recursión T(b/2) -> O(log2(b))
    res = matrix_modexp(matrix, b // 2)
    # Producto matricial es constante para dimensiones fijas -> O(1)
    return matrix_modmult(res, res)


if __name__ == "__main__":
    # Obtener N
    n_value = int(input())
    if n_value == 0:
        print(0)
    else:
        # Intución: https://stackoverflow.com/a/14272475
        print(sum_matrix(matrix_modexp(GRAPH_MATRIX, n_value)) % MOD)
