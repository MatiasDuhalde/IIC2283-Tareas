"""
Solución al problema 1 de la Tarea 2
"""
from os import read, fstat
from io import BytesIO
from copy import copy
import cmath
import math


DNA_CHARS = ["A", "T", "G", "C"]
CHAR_MAPPING = {
    "A": 1,
    "T": 2,
    "G": 3,
    "C": 4,
}

# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
# Copy read for multiple tests (comment for one test to save resources)
input_copy = copy(input_buffer)
input = input_buffer.readline


def rev(idx, length):
    ret = 0
    i = 0
    while (1 << i) < length:
        ret = ret << 1
        if idx & (1 << i):
            ret |= 1
        i += 1
    return ret


def fft(a, length, dft):
    """Fast Fourier Transform"""
    A = [0j] * length
    for i in range(length):
        A[rev(i, length)] = a[i]
    s = 1
    while (1 << s) <= length:
        m = 1 << s
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
    if dft == -1:
        for i in range(length):
            A[i] = A[i] / length
    return A


def work(char, s_string, t_string, length, k_error, answer):
    # Test function
    n = len(s_string)
    m = len(t_string)
    S = [0j] * length
    P = [0j] * length
    M = [0j] * length
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
        P[i] = ((t_string[i] == char) + 0j)
    S_fft = fft(S, length, 1)
    P_fft = fft(P, length, 1)
    for i in range(length):
        M[i] = S_fft[i] * P_fft[i]
    M_fft = fft(M, length, -1)
    curr_count = 0
    for i in range(length):
        res[i] = math.floor(M_fft[i].real + 0.5)
    for i in range(n):
        answer[i] += res[i]
    return res


def main():
    """Main function"""
    [s_length, t_length, k_error] = [int(x) for x in input().split()]
    s_string = input().strip().decode()
    t_string = input().strip().decode()
    length = 1
    while (length <= s_length):
        length *= 2
    length *= 2
    answer = [0] * length
    locations = {}
    for char in DNA_CHARS:
        if char in s_string and char in t_string:
            locations[char] = work(char, s_string, t_string, length, k_error, answer)

    # matches = 0
    # current_char_index = 0
    # current_char = t_string[0]
    # for k in range(s_length):
    #     if k in locations[current_char]:
    #         matches += locations[k][current_char_index]

    #     if k in locations:
    #     matches += 1
    # print(matches)

    res_count = 0
    current_count = 0
    for k in answer:
        if (k > 0):
            current_count += 1
        if (current_count == t_length):
            res_count += 1
            current_count = 0
    print(res_count)


if __name__ == '__main__':
    main()
