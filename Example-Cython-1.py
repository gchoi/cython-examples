"""
Example 1: Sum of Squares (Cython)
"""

import time, timeit
from cython_mods.sum_of_squares import fast_sum_of_squares


MAX_ITER = 20000

if __name__ == "__main__":
    result = fast_sum_of_squares(MAX_ITER)

    time_iterations = timeit.timeit(lambda: fast_sum_of_squares(MAX_ITER), number=1)
    print(f"Iterations for Sum of Squares: {MAX_ITER}")
    print(f"timeit: {time_iterations:.10f} (sec)")
