"""
Solucion al problema 1 de la Tarea 3
"""
from os import read, fstat
from io import BytesIO
from random import randint
from math import log

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
input = input_buffer.readline  # pylint: disable=redefined-builtin


ITERATIONS = 10


def jacobi(a_value, number):
    """
    Calcula el símbolo de Jacobi ( a_value | number )
    # Fuente: pseudocode de https://en.wikipedia.org/wiki/Jacobi_symbol

    Argumentos:
        a_value: int - a_value > 0
        number: int - impar > 0
    """
    t_value = 1
    while True:
        if number == 1:
            return t_value
        a_value = a_value % number
        if a_value == 0:
            return 0
        if a_value == 1:
            return t_value

        if a_value & 1 == 0:
            if number % 8 in (3, 5):
                t_value = -t_value
            a_value >>= 1
            continue

        if a_value % 4 == 3 and number % 4 == 3:
            t_value = -t_value

        a_value, number = number, a_value


def exp_mod(a_value: int, b_value: int, number: int) -> int:
    """
    Algoritmo de exponenciacion modular
    # Fuente: Mi tarea de IIC3253 2021-1
    # https://github.com/MatiasDuhalde/IIC3253-2021-1-MatiasDuhalde/blob/master/Tarea%202/Pregunta%202/pregunta2.ipynb

    Args:
        a_value: int - a_value >= 0
        b_value: int - b_value >= 0
        number: int - number > 0

    Returns:
        int: a_value**b_value mod number
    """
    if number == 1:
        return 0
    if b_value == 0:
        return 1
    a_value = a_value % number
    if a_value == 0:
        return 0
    c_value = 1
    while b_value > 0:
        if (b_value % 2) != 0:
            c_value = (c_value * a_value) % number
        b_value //= 2
        a_value = (a_value * a_value) % number
    return c_value


def gcd(a_value: int, b_value: int) -> tuple[int, int, int]:
    """
    Algoritmo de Euclides. Calcula GCD(a_value, b_value)

    Argumentos:
        a_value: int - a_value > 0
        b_value: int - a_value >= b_value > 0

    Retorna:
        int - GCD(a_value, b_value) maximo comun divisor GCD(a, b)
    """
    while b_value > 0:
        temp = b_value
        b_value = a_value % b_value
        a_value = temp
    return a_value


def solovay_strassen_test(number: int, k: int) -> bool:
    """
    Retorna True si number es primo, y False en caso contrario, con probabilidad de error de 2^(-k)
    si number es compuesto, y 0 si es primo.
    # Fuente: Algoritmo de clases + Paper de Solovay y Strassen
    # A Fast Monte-Carlo Test for Primality. Solovay, R; Strassen, V. SIAM Journal on Computing;
    # Philadelphia Tomo 6, N.º 1,  (Mar 1977): 2. DOI:10.1137/0206006
    # https://buscador.bibliotecas.uc.cl/permalink/f/cjn0ra/TN_cdi_proquest_journals_918499739

    Argumentos :
        number: int - n >= 1
        k: int - k >= 1
    Retorna:
        bool - True si n es probablemente un numero primo, y False en caso contrario.
    """
    if number == 2:
        return True
    if number % 2 == 0 or number == 1:
        return False
    for _ in range(k):
        random_a = randint(2, number - 1)
        gcd_a_n = gcd(random_a, number)
        if gcd_a_n > 1:
            return False
        epsilon = exp_mod(random_a, (number - 1) // 2, number)
        delta = jacobi(random_a, number) % number
        if epsilon != delta:
            return False
    return True


def get_prime(lower_bound: int, upper_bound: int, k=ITERATIONS) -> int:
    """
    Obtiene un numero probablemente primo entre lower_bound y upper_bound

    Argumentos :
        lower_bound: int - lower_bound >= 2
        upper_bound: int - upper_bound >= lower_bound
        k: int - k >= 1
    Retorna :
        int - numero primo entre lower_bound y upper_bound, -1 si no logra encontrarlo
    """
    if upper_bound % 2 == 0:
        upper_bound -= 1
    new_lower_bound = int(log(upper_bound))
    if new_lower_bound > lower_bound:
        lower_bound = new_lower_bound
    for number in range(upper_bound, lower_bound, -2):
        if solovay_strassen_test(number, k):
            return number
    return -1


def main():
    """Main function"""
    # Read input
    [a_value, b_value] = [int(x) for x in input().split()]

    # Solve
    result = get_prime(a_value, b_value)

    # Output result
    print(result)


if __name__ == '__main__':
    main()
