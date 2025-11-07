# cython: language_level=3
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION

import cython
from libc.stdlib cimport rand, RAND_MAX
import numpy as np
cimport numpy as np


@cython.boundscheck(False)
@cython.wraparound(False)
def sharpen_image_cython(np.ndarray[np.uint8_t, ndim=3] image_array) -> np.ndarray:
    # Define sharpening kernel
    cdef int kernel[3][3]
    kernel[0][0] = 0
    kernel[0][1] = -1
    kernel[0][2] = 0
    kernel[1][0] = -1
    kernel[1][1] = 5
    kernel[1][2] = -1
    kernel[2][0] = 0
    kernel[2][1] = -1
    kernel[2][2] = 0

    # Declare variables outside of loops
    cdef int height = image_array.shape[0]
    cdef int width = image_array.shape[1]
    cdef int channel, i, j, ki, kj
    cdef int value

    # Prepare an empty array for the sharpened image
    cdef np.ndarray[np.uint8_t, ndim=3] sharpened_array = np.zeros_like(image_array)

    # Convolve each channel separately
    for channel in range(3):  # Iterate over RGB channels
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                value = 0  # Reset value at each pixel
                # Apply the kernel
                for ki in range(-1, 2):
                    for kj in range(-1, 2):
                        value += kernel[ki + 1][kj + 1] * image_array[i + ki, j + kj, channel]
                # Clip values to be between 0 and 255
                sharpened_array[i, j, channel] = min(max(value, 0), 255)

    return sharpened_array
