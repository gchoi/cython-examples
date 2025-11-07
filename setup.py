# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np


module_list = [
    "sum_of_squares.pyx",
    "monte_carlo.pyx",
    "image_processor.pyx"
]

setup(
    name="cython-test",
    ext_modules=cythonize(module_list=module_list, language_level=3),
    py_modules=["sum_of_squares"],  # Explicitly state the module
    zip_safe=False,
    include_dirs=[np.get_include()]
)
