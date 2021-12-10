"""
Solucion al problema 2 de la Tarea 3
"""
from os import read, fstat
from io import BytesIO
from math import ceil, comb, log10

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
input = input_buffer.readline  # pylint: disable=redefined-builtin


def sieve_of_erathostenes(n_value):
    """
    Criba de Eratostenes modificada para obtener coprimos menores de n_value

    Argumentos:
        n_value: int - Numero sobre el que se quiere obtener los coprimos (menores)

    Retorna:
        List[int] - Lista de numeros coprimos de n_value (menores)
    """
    result = [True] * (n_value)
    result[0] = False
    for i in range(2, n_value // 2 + 1):
        if n_value % i == 0:
            result[i] = False
            for j in range(i * 2, n_value, i):
                result[j] = False
    return [i for i in range(len(result)) if result[i]]


def main():
    """Main function"""
    # Read input
    [n_value, k_value] = [int(x) for x in input().split()]

    # Get coprimes
    result = sieve_of_erathostenes(n_value)

    # Get combinations
    n_combs = comb(len(result), k_value)

    if n_combs == 0:
        # Output result
        print(-1)
    else:
        # Get least significant digit
        lsd = 0
        for _ in range(ceil(log10(n_combs)) + 1):
            lsd = n_combs % 10
            if lsd != 0:
                break
            n_combs //= 10
        print(lsd)


if __name__ == '__main__':
    main()
