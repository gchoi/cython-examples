# sun_of_squares.pyx
def fast_sum_of_squares(int n) -> int:
    cdef int total = 0
    cdef int i, j
    for i in range(n):
        for j in range(n):
            total += i * i + j * j
    return total
