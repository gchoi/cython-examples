import cython
from libc.stdlib cimport rand, RAND_MAX


@cython.boundscheck(False)
@cython.wraparound(False)
def monte_carlo_pi(int num_samples) -> double:
    if num_samples <= 0:
        raise ValueError("num_samples must be positive")

    cdef int inside_circle = 0
    cdef int i
    cdef double x, y

    for i in range(num_samples):
        x = rand() / <double>RAND_MAX
        y = rand() / <double>RAND_MAX
        if (x**2) + (y**2) <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4
