"""
Solucion al problema 2 de la Tarea 2
"""
from collections import defaultdict
from os import read, fstat
from io import BytesIO
from random import choices
from math import ceil, log10
from copy import copy

EPSILON = 1e-3
ITERATIONS = 3


# Use fast read
input_buffer = BytesIO(read(0, fstat(0).st_size))
# Copy read for multiple tests (comment for one test to save resources)
input_copy = copy(input_buffer)
input = input_buffer.readline


def main():
    """Main function"""
    # Read input
    [n_value, m_value, p_value] = map(int, input().split())
    binary_values = []
    for _ in range(n_value):
        binary_values.append(int(input().strip(), 2))

    # Solve
    # Iterate times
    results = defaultdict(int)
    for _ in range(10**(ITERATIONS)):
        current = 2**m_value - 1
        subset = choices(binary_values, k=2*ceil(log10(n_value + 1)))
        for el in subset:
            current = current & el
        results[current] += 1
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    [value, reps] = sorted_results[0]
    if (value == 0):
        try:
            [value, reps] = sorted_results[1]
        except:
            pass
    binary_result = format(value, f"0{m_value}b")
    print(binary_result)
    return binary_result


if __name__ == '__main__':
    # Test once
    main()

    # Test several
    # TEST_NUMBER = 100
    # TEST_RESULT = "000000010000100000000000010001000000000000000000010010001100"
    # counter = 0
    # for _ in range(TEST_NUMBER):
    #     input_buffer = input_copy
    #     input = input_buffer.readline
    #     input_copy = copy(input_copy)
    #     res = main()
    #     if res != TEST_RESULT:
    #         counter += 1
    # print("Desired error:", EPSILON)
    # print("Actual error:", counter/TEST_NUMBER)
    # print("Accomplished:", counter/EPSILON <= EPSILON)
