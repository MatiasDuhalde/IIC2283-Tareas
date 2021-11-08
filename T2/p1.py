"""
Solucion al problema 1 de la Tarea 2
"""
from os import read, fstat
from io import BytesIO
import cmath
import math


DNA_CHARS = ["A", "T", "G", "C"]

EXPONENTS_TABLE = {}

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
input = input_buffer.readline

# global
answer = []


def recursive_fft(a):
    """
    Algorithm based on Wikipedia pseudocode (recursive)
    https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
    """
    n = len(a)

    if n == 2:
        x_0, x_1 = a
        return [x_0 + x_1, x_0 - x_1]

    n_half = n // 2

    X_0 = recursive_fft(a[:n:2])
    X_1 = recursive_fft(a[1:n:2])

    X = [0] * n

    for k in range(n_half):
        p = X_0[k]
        q = cmath.exp(cmath.pi * 2j * k / n) * X_1[k]
        X[k] = p + q
        X[n_half + k] = p - q
    return X


def work(char, s_string, t_string, length, k_error):
    """
    Verify a char over the input strings
    """
    # Obtain lengths
    n = len(s_string)
    m = len(t_string)
    # Define arrays (memory complexity?)
    S = [0] * length
    T = [0] * length
    M = [0] * length
    res = [0] * length
    # Complexity ??
    # Check s_string possibilities
    if char in s_string[0:k_error]:
        char_range = k_error
    else:
        char_range = None
    for i in range(n):
        if (s_string[i] == char or (i + k_error < n and s_string[i + k_error] == char)):
            char_range = k_error
        if (char_range is not None and char_range >= 0):
            S[i] = 1
        if char_range is None:
            char_range = 0
        char_range -= 1
    # Check t_string possibilities (inverted)
    for i in range(m):
        T[m - 1 - i] = int(t_string[i] == char)
    # Get overlaps with FFT
    S_fft = recursive_fft(S)
    T_fft = recursive_fft(T)
    M = [x * y for x, y in zip(S_fft, T_fft)]
    # Inverse FFT
    M_fft = recursive_fft([M[0]] + list(reversed(M[1:])))
    M_n = len(M_fft)
    # Finish inverse + save results to answer global
    for i, x in enumerate(M_fft):
        answer[i] += math.floor(x.real / M_n + 0.5)
    return res


def main():
    """Main function"""
    # read input
    [s_length, t_length, k_error] = [int(x) for x in input().split()]
    s_string = input().strip().decode()
    t_string = input().strip().decode()

    # Get length
    length = 2**math.ceil(math.log2(s_length + t_length))

    # Define global answer
    global answer
    answer = [0] * length

    # Solve for every char
    for char in DNA_CHARS:
        work(char, s_string, t_string, length, k_error)

    # Join answers
    print(sum([1 for i in range(s_length) if answer[i] == t_length]))


if __name__ == '__main__':
    main()
