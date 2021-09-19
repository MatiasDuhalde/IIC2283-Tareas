"""
Solución a problema 1:
Dado un número N entero positivo, entregar la cantidad de caminos que pasan
por N aristas, en el multigrafo que representa al problema de los siete puentes
de Königsberg.
"""
import sys

# Grafo
GRAPH = {
    0: [1, 1, 2],
    1: [0, 0, 2, 3, 3],
    2: [0, 1, 3],
    3: [1, 1, 2],
}

# Cache
CACHE = {
    0: {0: 1},
    1: {0: 1},
    2: {0: 1},
    3: {0: 1}
}


def get_node_path_number(node, n):
    cache_res = CACHE[node].get(n)
    if cache_res:
        return cache_res
    else:
        res = 0
        for next_node in GRAPH[node]:
            res += get_node_path_number(next_node, n - 1)
            res %= (10 ** 9 + 7)
        CACHE[node][n] = res
        return res


if __name__ == "__main__":
    # Obtener N
    n_value = int(input("N: "))

    sys.setrecursionlimit(10000)

    result = 0
    for node in GRAPH:
        result += get_node_path_number(node, n_value)
        result %= (10 ** 9 + 7)

    print(result)
