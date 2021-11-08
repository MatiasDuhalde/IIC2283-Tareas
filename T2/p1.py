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
    A = [complex()] * length
    for i in range(length):
        A[rev(i)] = a[i]
    s = 1
    m = 1 << s
    while m <= length:
        wm = complex(cmath.cos(dft * 2 * cmath.pi / m), cmath.sin(dft * 2 * cmath.pi / m))
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
    if dft == -1:
        for i in range(length):
            A[i] /= length
    return A


def work(char, s_string, t_string, length, k_error):
    n = s_length
    m = t_length
    S = [complex()] * length
    T = [complex()] * length
    M = [complex()] * length
    res = [0] * length
    if char in s_string[0:k_error]:
        char_range = k_error
    else:
        char_range = None
    for i in range(n):
        if (s_string[i] == char or (i + k_error < n and s_string[i + k_error] == char)):
            char_range = k_error
        if (char_range is not None and char_range >= 0):
            S[i] = complex(1, 0)
        if char_range is None:
            char_range = 0
        char_range -= 1
    for i in range(m):
        T[m - 1 - i] = complex(t_string[i] == char, 0)
    S_fft = fft(S, length, 1)
    T_fft = fft(T, length, 1)
    for i in range(length):
        M[i] = S_fft[i] * T_fft[i]
    M_fft = fft(M, length, -1)
    for i, x in enumerate(M_fft):
        answer[i] += math.floor(x.real + 0.5)
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
    padding = math.ceil(math.log2(2*s_length))
    length = 2**padding
    answer = [0] * length
    for char in DNA_CHARS:
        work(char, s_string, t_string, length, k_error)

    # Optimized
    print(sum([1 for i in range(s_length) if answer[i] == t_length]))


if __name__ == '__main__':
    main()
