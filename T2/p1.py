"""
Solucion al problema 1 de la Tarea 2
"""
from os import read, fstat
from io import BytesIO
from copy import copy
import cmath
import math


DNA_CHARS = ["A", "T", "G", "C"]

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
# Copy read for multiple tests (comment for one test to save resources)
input_copy = copy(input_buffer)
input = input_buffer.readline

# global
padding = 0
answer = []
s_length = 0
t_length = 0


def rev(n):
    res = int(format(n, f"0{padding}b")[::-1], 2)
    return res


def fft(a, length, dft):
    """Fast Fourier Transform"""
    A = [0] * length
    for i in range(length):
        A[rev(i)] = a[i]
    s = 1
    m = 1 << s
    while m <= length:
        wm = complex(cmath.cos(-dft * 2 * cmath.pi / m), cmath.sin(-dft * 2 * cmath.pi / m))
        for k in range(0, length, m):
            w = complex(1, 0)
            j = 0
            while j < (m >> 1):
                t = w * A[k + j + (m >> 1)]
                u = A[k + j]
                A[k + j] = u + t
                A[k + j + (m >> 1)] = u - t
                w = w * wm
                j += 1
        s += 1
        m = 1 << s
    return A


def recursive_fft(a):
    n = len(a)

    if n == 2:
        a_0, a_1 = a
        return [a_0 + a_1, a_0 - a_1]

    n_half = n // 2

    y_0 = recursive_fft(a[:n:2])
    y_1 = recursive_fft(a[1:n:2])

    res = [0] * n

    for k in range(n_half):
        a = y_0[k]
        b = cmath.exp(cmath.pi * 2j * k / n) * y_1[k]
        res[k] = a + b
        res[n_half + k] = a - b
    return res


def fft2(a, length, dft):
    """Fast Fourier Transform"""
    A = [0] * length
    for i in range(length):
        A[rev(i)] = a[i]
    for s in range(1, int(math.log2(length)) + 1):
        m = 2**s
        wm = cmath.exp(dft * -2j * cmath.pi / m)
        for k in range(0, length, m):
            w = complex(1, 0)
            for j in range(m // 2):
                t = w * A[k + j + m // 2]
                u = A[k + j]
                A[k + j] = u + t
                A[k + j + m // 2] = u - t
                w = w * wm
    if dft == -1:
        for i in range(length):
            A[i] /= length
    return A


def work(char, s_string, t_string, length, k_error):
    n = s_length
    m = t_length
    S = [0] * length
    T = [0] * length
    M = [0] * length
    res = [0] * length
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
    for i in range(m):
        T[m - 1 - i] = int(t_string[i] == char)
    S_fft = recursive_fft(S)
    T_fft = recursive_fft(T)
    M = [x * y for x, y in zip(S_fft, T_fft)]
    M_fft = recursive_fft([M[0]] + list(reversed(M[1:])))
    M_n = len(M_fft)
    for i, x in enumerate(M_fft):
        answer[i] += math.floor(x.real / M_n + 0.5)
    return res


def main():
    """Main function"""
    global s_length
    global t_length
    [s_length, t_length, k_error] = [int(x) for x in input().split()]
    s_string = input().strip().decode()
    t_string = input().strip().decode()

    global padding
    global answer
    padding = math.ceil(math.log2(s_length + t_length))
    length = 2**padding
    answer = [0] * length
    for char in DNA_CHARS:
        work(char, s_string, t_string, length, k_error)

    # Optimized
    print(sum([1 for i in range(s_length) if answer[i] == t_length]))


if __name__ == '__main__':
    main()
