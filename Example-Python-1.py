"""
Example 1: Sum of Squares (Standard Python)
"""

import timeit


MAX_ITER = 20000

def slow_sum_of_squares(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * i + j * j
    return total


if __name__ == "__main__":
    time_iterations = timeit.timeit(lambda: slow_sum_of_squares(MAX_ITER), number=1)
    print(f"Iterations for Sum of Squares: {MAX_ITER}")
    print(f"timeit: {time_iterations:.10f} (sec)")
